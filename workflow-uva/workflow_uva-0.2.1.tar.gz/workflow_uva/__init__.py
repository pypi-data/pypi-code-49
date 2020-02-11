import csv
import os
import re
import json
import shutil
import subprocess
import nbformat
import sys
import urllib.request
import warnings
import itertools

import matplotlib.pyplot as plt
from notebook import notebookapp
import nbconvert
import nbgrader
from nbconvert.preprocessors import CellExecutionError, ExecutePreprocessor
import numpy as np
import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup
from canvasapi import Canvas
from collections import defaultdict, Counter
from IPython.display import Javascript, Markdown, display, clear_output
from ipywidgets import (Button, Layout, fixed, interact, interact_manual,
                        interactive, widgets)
from nbgrader.apps import NbGraderAPI
from tqdm import tqdm, tqdm_notebook  # Progress bar
from traitlets.config import Config
warnings.filterwarnings('ignore')


class Course:
    canvas_course = None
    filename = 'workflow.json'

    resits = {}
    groups = {}
    sequence = []
    requirements = []

    def __init__(self):
        if self.filename in os.listdir():
            self.load_pickle()
        else:
            self.gradedict = {}
        if self.canvas_course is None:
            if "key" not in self.__dict__.keys() or "url" not in self.__dict__.keys(
            ) or "canvas_id" not in self.__dict__.keys():
                change_canvas_credentials()
            else:
                self.log_in(self.canvas_id, self.url, self.key)

        config = Config()
        config.Exchange.course_id = os.getcwd().split('\\')[-1]
        self.nbgrader_api = NbGraderAPI(config=config)

    def change_canvas_credentials(
            self,
            canvas_id='',
            url="https://canvas.uva.nl",
            key=''):
        if "key" in self.__dict__.keys():
            key = self.key
        if "url" in self.__dict__.keys():
            url = self.url
        if "canvas_id" in self.__dict__.keys():
            canvas_id = self.canvas_id
        login_button = interact_manual.options(
            manual_name="Log in to Canvas")
        login_button(
            self.log_in,
            canvas_id=canvas_id,
            url=url,
            key=key)

    def show_course_settings(self):
        """Prints the course settings"""
        
        list_of_assignments = []
        enddict = defaultdict(list)
        
        for k, v in self.resits.items():
            if isinstance(v, list):
                for assignment in v:
                    enddict[assignment].append(k)
            elif isinstance(v, str):
                enddict[v].append(k)
                
        for k, v in self.groups.items():
            weight = round(v["weight"] / len(v["assignments"]), 2)
            for assignment in v["assignments"]:
                if assignment in self.sequence:
                    index = self.sequence.index(assignment)
                else:
                    index = np.nan
                if assignment in enddict:
                    resits = [
                        x for x in self.sequence if x in enddict[assignment]]
                else:
                    resits = np.nan
                if assignment in self.gradedict:
                    min_grade = self.gradedict[assignment]['min_grade']
                    max_score = self.gradedict[assignment]['max_score']
                else:
                    if assignment in (
                            x.name for x in self.nbgrader_api.gradebook.assignments):
                        min_grade = 0
                        max_score = self.nbgrader_api.gradebook.find_assignment(
                            assignment).max_score
                    else:
                        min_grade = np.nan
                        max_score = np.nan
                list_of_assignments.append([k, assignment, index, resits,
                                weight, min_grade, max_score])
        
        for resit in self.resits:
            if resit in self.gradedict:
                min_grade = self.gradedict[resit]['min_grade']
                max_score = self.gradedict[resit]['max_score']
            else:
                if resit in (
                        x.name for x in self.nbgrader_api.gradebook.assignments):
                    min_grade = 0
                    max_score = self.nbgrader_api.gradebook.find_assignment(
                        resit).max_score
                else:
                    min_grade = np.nan
                    max_score = np.nan

            if resit in self.sequence:
                index = self.sequence.index(resit)
            else:
                index = np.nan
            if resit in enddict:
                resits = enddict[resit]
            else:
                resits = np.nan
            list_of_assignments.append(["Resits", resit, index, resits,
                            np.nan, min_grade, max_score])
        df = pd.DataFrame(
            list_of_assignments,
            columns=[
                "Group",
                "Assignment",
                "Order",
                "Resits",
                "Weight",
                "Minimal Grade",
                "Points needed for a 10"])
        display(df.set_index(["Group", "Assignment"]))
        
        # Prints all the requirements
        print("To pass a course a student has to")
        for requirement in self.requirements:
            if isinstance(requirement["groups"], str):
                print(
                    "\thave a minimal mean grade of {:.1f} for {}".format(
                        requirement["min_grade"], requirement["groups"]))
            elif isinstance(r["groups"], list):
                if len(requirement['groups']) == 1:
                    print(
                        "\thave a minimal mean grade of {:.1f} for {}".format(
                            requirement['min_grade'], requirement['groups']))
                elif len(requirement["groups"]) > 1:
                    print("\thave a minimal mean grade of {:.1f} for {} and {}".format(
                        requirement['min_grade'], ", ".join(requirement['groups'][:-1]), requirement['groups'][-1]))
        print("\thave a minimal weighted mean grade of 5.5 for all groups")

    def log_in(self, canvas_id, url, key):
        try:
            canvas_obj = Canvas(url, key)
            self.canvas_course = canvas_obj.get_course(int(canvas_id))
            self.canvas_id = canvas_id
            self.url = url
            self.key = key
            self.save_pickle()

            print("Logged in succesfully")
            print("Course name: %s\nCourse code: %s" %
                  (self.canvas_course.name, self.canvas_course.course_code))
            print("Canvas course id: %s" % canvas_id)
            print("Username: %s" % (canvas_obj.get_current_user().name))
            change_login_button = Button(
                description="Change course/user",
                layout=Layout(width='300px'))
            change_login_button.on_click(self.change_canvas_credentials)
            display(change_login_button)
        except ValueError:
            print("Course id should be an integer")
            self.change_canvas_credentials()
        except InvalidAccessToken:
            print("Incorrect key")
            change_canvas_credentials()

    def load_pickle(self):
        f = open(self.filename, 'r')
        tmp_dict = json.load(f)
        f.close()
        self.__dict__.update(tmp_dict)

    def save_pickle(self):
        """Saved changed variables in class to json-file"""
        f = open(self.filename, 'w')
        temp = {
            k: v for k,
            v in self.__dict__.items() if type(v) in [
                str,
                list,
                dict,
                int,
                float]}
        json.dump(temp, f, indent=4, sort_keys=True)
        f.close()

    def button_db(self):
        """Displays button which upon click updates students in the database"""
        if self.canvas_course is None:
            print("Updating students is only available when connected to Canvas")
            return
        db_button = Button(
            description="Update the students in the database",
            layout=Layout(width='300px'))
        db_button.on_click(self.update_db)
        return db_button

    def update_db(self, b):
        """Update the student information from canvas into nbgrader database"""
        for student in tqdm_notebook(
                self.canvas_course.get_users(enrollment_type=['student'])):
            first_name, last_name = student.name.split(' ', 1)

            self.nbgrader_api.gradebook.update_or_create_student(
                str(student.sis_user_id),
                first_name=first_name,
                last_name=last_name)

    def assign_button(self):
        interact_assign = interact_manual.options(
            manual_name="Assign assignment")

        return interact_assign(
            self.assign,
            assignment_id=self.nbgrader_assignments(),
            run_to_check_for_errors=False,
            header_file="")

    def assign(self, assignment_id, run_to_check_for_errors, header_file):
        file = 'source/' + assignment_id + '/' + assignment_id + ".ipynb"
        assert os.path.exists(
            file), "The folder name and notebook name are not equal."
        
        # Run nbgrader update to avoid conflicting versions
        subprocess.run(["nbgrader", "update", file])
        
        # Create the query
        query = ["nbgrader", "generate_assignment", assignment_id, "--create", "--force"]
        
        # If a header file is provided, include in query
        if header_file != "":
            assert os.path.exists(header_file), "The header file '%s' does not exist" %header_file
            query.append("--IncludeHeaderFooter.header=%s" %header_file)
        
        subprocess.run(query)
        
        # If chosen, execute the file to check for errors
        if run_to_check_for_errors:
            print("Checking for errors..")
            with open("nbgrader_config.py") as f:
                contents = f.read()
                timer = 30
                if "ExecutePreprocessor.timeout" in contents:
                    timer = min(
                        int(x) for x in re.findall(
                            r'ExecutePreprocessor\.timeout\s*=\s*(\d*)',
                            contents))
            ep = ExecutePreprocessor(timeout=timer, kernel_name='python3')
            with open(file, encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)
                try:
                    out = ep.preprocess(
                        nb, {'metadata': {'path': 'source/%s/' % assignment_id}})
                except CellExecutionError:
                    out = None
                    print("Error executing the notebook %s .\nSee notebook for the traceback." % file)
                except TimeoutError:
                    print("Timeout (after %s seconds) in on of the cells" % timer)
                    print("Consider changing the timeout in nbgrader_config.py")
                finally:
                    with open(file, mode='w', encoding='utf-8') as f:
                        nbformat.write(nb, f)
                    print("No errors found! :)")
        # If canvas is used and there is no assignment on canvas, create
        if self.canvas_course is not None:
            assignmentdict = {
                assignment.name: assignment.id
                for assignment in self.canvas_course.get_assignments()
            }

            if assignment_id not in assignmentdict.keys():
                self.canvas_course.create_assignment(
                    assignment={
                        'name': assignment_id,
                        'points_possible': 10,
                        'submission_types': 'online_upload',
                        'allowed_extensions': 'ipynb',
                        'published': 'True'
                    })

    def nbgrader_assignments(self):
        """Returns a sorted list of assignments in nbgrader"""
        return sorted([
            assignment
            for assignment in self.nbgrader_api.get_source_assignments()
        ])

    def download_button(self):
        interact_download = interact_manual.options(
            manual_name="Download files")
        return interact_download(
            self.download_files, assignment_id=self.nbgrader_assignments())

    def download_files(self, assignment_id):
        """Downloads all the files from Canvas for an assignment
        If none were found on Canvas, uses zip collect in the download folder"""
        if self.canvas_course is not None:
            if assignment_id in [
                    assignment.name
                    for assignment in self.canvas_course.get_assignments()
            ]:
                # Get sis id's from students
                student_dict = self.get_student_ids()

                # Get the Canvas assignment id
                assignment = self.get_assignment_obj(assignment_id)
                groups = []

                for submission in tqdm_notebook(
                    assignment.get_submissions(
                        include=['group'])):
                    if submission.group['id'] is not None:
                        if submission.group['id'] in groups:
                            continue
                        else:
                            groups.append(submission.group['id'])
                            
                    # Check if submission has attachments
                    if 'attachments' not in submission.attributes:
                        continue
                        
                    # Download file and give correct name
                    student_id = student_dict[submission.user_id]
                    attachment = submission.attributes["attachments"][0]

                    directory = "submitted/%s/%s/" % (student_id,
                                                      assignment_id)
                    if not os.path.exists(directory):
                        os.makedirs(directory)

                    filename = assignment_id + ".ipynb"
                    urllib.request.urlretrieve(attachment['url'],
                                               directory + filename)
                    
                    # Clear all notebooks of output to save memory
                    subprocess.run(["nbstripout", directory + filename])
                    subprocess.run(["nbgrader", "update", directory + filename])
                    
        else:
            print("No assignment found on Canvas")
            
        # Move the download files to submission folder
        if os.path.exists('downloaded/%s/' % (assignment_id)):
            for file in os.listdir('downloaded/%s/' % (assignment_id)):
                pass
            print("Zip-collect will run, see terminal for more info")
            subprocess.run([
                "nbgrader", "zip_collect", assignment_id, "--force",
                "--log-level='INFO'"
            ])

    def get_assignment_obj(self, assignment_name):
        return {
            assignment.name: assignment
            for assignment in self.canvas_course.get_assignments()
        }[assignment_name]

    def autograde_button(self):
        """Returns button that on click starts autograding selected assignment"""
        interact_autograde = interact_manual.options(manual_name="Autograde")
        return interact_autograde(
            self.autograde, assignment_id=self.nbgrader_assignments())

    def autograde(self, assignment_id):
        """Autograde assignment"""
        
        # Creates a custom progressbar
        pbar = tqdm_notebook(
            sorted(
                self.nbgrader_api.get_submitted_students(assignment_id)))
        
        for student in pbar:
            pbar.set_description("Currently grading: %s" % student)
            subprocess.run([
                "nbgrader", "autograde", assignment_id, "--create", "--force",
                "--student=%s" %("'" + student + "'")
            ])
            
        # Create widget to link to manual grading in formgrader
        localhost_url = [x['url'] for x in notebookapp.list_running_servers(
        ) if x["notebook_dir"] == os.getcwd()][0]
        
        display(
            Markdown(
                '<a class="btn btn-primary" style="margin-top: 10px; text-decoration: none;" href="%sformgrader/gradebook/%s/%s" target="_blank">Klik hier om te manual graden</a>' %
                (localhost_url, assignment_id, assignment_id)))

    def plagiat_button(self):
        """Returns interact that on click checks for plagiarism in selected assignment"""
        interact_plagiat = interact_manual.options(
            manual_name="Check for plagiarism")
        return interact_plagiat(
            self.plagiarism_check,
            assignment_id=self.nbgrader_assignments())

    def plagiarism_check(self, assignment_id):
        """Checks for plagiarism in given assignment"""
        # Remove old plagiarism checks for assignment
        if os.path.exists("plagiarismcheck/%s/" % assignment_id):
            shutil.rmtree(
                "plagiarismcheck/%s/" % assignment_id, ignore_errors=True)
            
        # Create folders
        os.makedirs("plagiarismcheck/%s/pyfiles/" % assignment_id)
        os.makedirs("plagiarismcheck/%s/base/"% assignment_id)
        
        # Convert and move release to plagiarismcheck folder
        exporter = nbconvert.PythonExporter()
        source_file = exporter.from_filename(
            "release/%s/%s.ipynb" % (assignment_id, assignment_id))
        target_file = open(
            "plagiarismcheck/%s/base/%s.py" % (assignment_id, assignment_id),
            "w", encoding="utf-8")
        target_file.write(source_file[0])
        target_file.close()
        
        # Convert and move submitted assignments to plagiarismcheck folder
        for student in tqdm_notebook(
                self.nbgrader_api.get_submitted_students(assignment_id),
                desc="Converting notebooks to .py"):
            source_file = exporter.from_filename(
                "submitted/%s/%s/%s.ipynb" %
                (student, assignment_id, assignment_id))
            target_file = open(
                "plagiarismcheck/%s/pyfiles/%s_%s.py" %
                (assignment_id, student, assignment_id), "w", encoding="utf-8")
            target_file.write(source_file[0])
            target_file.close()
        
        # Try to run compare50, otherwise recommend to install
        try:
            subprocess.run(["compare50", "plagiarismcheck/%s/pyfiles/*" %
                            assignment_id, "-d", "plagiarismcheck/%s/base/*" %
                            assignment_id, "-o", "plagiarismcheck/%s/html/" %
                            assignment_id])

        except BaseException:
            print(
                "Install check50 for plagiarism check. (This is not available on Windows)")
        display(
            Markdown(
                '<a class="btn btn-primary" style="margin-top: 10px; text-decoration: none;" href="plagiarismcheck/%s/" target="_blank">Open folder with results of plagiarism check</a>' %
                assignment_id))

    def color_grades(self, row):
        """Return either green or red based on the grade"""
        if row['interval'].right <= 5.5:
            return 'r'
        else:
            return 'g'

    def grades_button(self):
        return interact(
            self.interact_grades, assignment_id=self.graded_submissions())

    def visualize_grades(self, assignment_id, min_grade, max_score):
        """Creates a plot of the grades from a specific assignment"""
        if assignment_id is None:
            print("No assignment selected")
            return

        # Get grades from nbgrader database
        grades = self.create_grades_per_assignment(assignment_id, min_grade,
                                                   max_score)[assignment_id]

        # Only select grades from submissions that have been autograded
        index = (submission["student"]
                 for submission in self.nbgrader_api.get_submissions(assignment_id)
                 if submission["autograded"])
        grades = grades.reindex(index, axis='index').dropna()

        # Print a few statistics about the grades
        print("The mean grade is {:.1f}".format(grades.mean()))
        print("The median grade is {}".format(grades.median()))
        print("Maximum of Cohen-Schotanus is {:.1f}".format(
            grades.nlargest(max(1, int(len(grades) * 0.05))).mean()))
        print("The percentage insufficent grades is {:.1f}%. ".format(
            100 * sum(grades < 5.5) / len(grades)))

        bins = np.arange(1, 10, 0.5)
        interval = [pd.Interval(x, x + 0.5, closed='left') for x in bins]
        interval[-1] = pd.Interval(left=9.5, right=10.001, closed='left')
        interval = pd.IntervalIndex(interval)
        grades_by_interval = pd.DataFrame(
            grades.groupby([pd.cut(grades, interval)]).size())
        grades_by_interval.columns = ["frequency"]
        grades_by_interval = grades_by_interval.reset_index()
        grades_by_interval.columns = ["interval", "frequency"]
        grades_by_interval['color'] = grades_by_interval.apply(
            self.color_grades, axis=1)

        # Plot the grades
        sns.set(style="darkgrid")
        fig, ax = plt.subplots()
        ax.set_xlim(1, 10)
        ax.xaxis.set_ticks(range(1, 11))
        ax2 = ax.twinx()
        ax2.yaxis.set_ticks([])
        ax.bar(
            bins,
            grades_by_interval['frequency'],
            width=0.5,
            align="edge",
            color=grades_by_interval['color'])
        sns.kdeplot(grades, ax=ax2, clip=(1, 10), legend=False)
        plt.show()
        
        # Create button to change settings
        grades_button = Button(
            description="Save grades", layout=Layout(width='300px'))
        grades_button.on_click(self.update_grades)
        self.curr_assignment = assignment_id
        self.curr_grade_settings = {
            "max_score": max_score,
            "min_grade": min_grade
        }
        display(grades_button)
        
        self.percentiles(grades, assignment_id)

    def percentiles(self, df, assignment):
        dec = df.quantile(np.arange(11) / 10)
        dec.index = (dec.index * 100).astype(int)
        dec.plot(
            kind='barh',
            title='%s: Which grade gets into what percentile.' %
            assignment,
            xlim=(
                1,
                10))

    def item_button(self):
        """Returns button to select assignment for item analysis visualisations"""
        return interact(
            self.question_visualizations,
            assignment_id=self.graded_submissions())

    def update_grades(self, b):
        """"Changes the gradings settings for assignment
        and saves in json file"""
        self.gradedict[self.curr_assignment] = self.curr_grade_settings
        self.save_pickle()

    def p_value(self, df):
        """Given a dataframe, calculates the p-value for each question"""
        return df.groupby(
            'question_name', sort=False)['score'].mean() / df.groupby(
                'question_name', sort=False)['max_score'].mean()

    def create_grades_per_assignment(self,
                                     assignment_name,
                                     min_grade=None,
                                     max_score=None):
        """Returns a dataframe with the grades for an assignment"""
        
        # Get min_grade and max_score if not provided
        if min_grade is None and max_score is None:
            min_grade, max_score, _ = self.get_default_grade(
                assignment_name)

        # Return nothing if max_score is 0
        if max_score == 0:
            return
        
        # Get the raw scores from gradebook
        canvasdf = pd.DataFrame(
            self.nbgrader_api.gradebook.submission_dicts(
                assignment_name)).set_index('student')
        
        # Calculate the grade
        canvasdf['grade'] = canvasdf['score'].apply(
            lambda row: self.calculate_grade(row, min_grade, max_score))
        canvasdf = canvasdf.pivot_table(
            values='grade', index='student', columns='name', aggfunc='first')
        return canvasdf

    def total_df(self):
        """Returns a df with grades of all graded assignments"""
        list_of_dfs = [
            self.create_grades_per_assignment(assignment)
            for assignment in self.graded_submissions()]

        # Remove assignments without grades
        list_of_dfs = [assignment_df for assignment_df in list_of_dfs
                       if assignment_df is not None]
        if len(list_of_dfs) == 0:
            return None
        canvasdf = pd.concat(list_of_dfs,
                             axis=1)
        return canvasdf

    def calculate_grade(self, score, min_grade, max_score):
        """Calculate grade for an assignment"""
        return max(
            1,
            min(
                round(min_grade + (10 - min_grade) * score / max_score, 1),
                10.0))

    def graded_submissions(self):
        """Returns a list of graded submissions"""
        return [
            x['name'] for x in self.nbgrader_api.get_assignments()
            if x['num_submissions'] > 0
        ]

    def create_results_per_question(self):
        """Returns a dataframe with the score and max_score per grading cell per student"""
        list_of_grades_per_cell = []
        for assignment in self.nbgrader_api.gradebook.assignments:
            for notebook in assignment.notebooks:
                for cell in notebook.task_cells + notebook.grade_cells:
                    for grade in cell.grades:
                        list_of_grades_per_cell.append([assignment.name, grade.student.id, grade.score, grade.max_score,cell.name])
        return pd.DataFrame(list_of_grades_per_cell, columns = ["assignment","student_id","score","max_score","question_name"])

    def interact_grades(self, assignment_id):
        """Displays a widget to select a minimum grade and maximum score"""
        score_list = self.get_default_grade(assignment_id)
        
        # Check if there are grades in database
        if score_list is None:
            print("No grades in the database")
            return

        min_grade, max_score, abs_max = score_list
        if max_score == 0:
            print("No grades in the database")
            return
        
        interact(
            self.visualize_grades,
            assignment_id=fixed(assignment_id),
            min_grade=widgets.FloatSlider(
                value=min_grade,
                min=0,
                max=9.5,
                step=0.5,
                continuous_update=False),
            max_score=widgets.FloatSlider(
                value=max_score,
                min=0.5,
                max=abs_max,
                step=0.5,
                continuous_update=False))

    def get_default_grade(self, assignment_id):
        """Get the current min_grade and max_score for an assignment"""
        if assignment_id == None:
            return None
        assignment = self.nbgrader_api.gradebook.find_assignment(assignment_id)
        
        if assignment.num_submissions == 0:
            return None
        
        # Set default values
        abs_max = assignment.max_score
        max_score = abs_max
        min_grade = 0
        
        # Get the grades from gradedict if they are in it
        if assignment_id in self.gradedict.keys():
            if 'max_score' in self.gradedict[assignment_id].keys():
                max_score = self.gradedict[assignment_id]['max_score']

            if 'min_grade' in self.gradedict[assignment_id].keys():
                min_grade = self.gradedict[assignment_id]['min_grade']            

        return min_grade, max_score, abs_max

    def question_visualizations(self, assignment_id):
        """Creates visualisations with the p-value and rir-value for an assignment"""
        # Get the questions and results for an assignment
        df = self.create_results_per_question()
        df = df.loc[df['assignment'] == assignment_id]
        df = df[df['max_score'] > 0]
        
        if df.empty:
            print("No graded cells found for this assignment")
            return
        
        # Calculate and combine p value and rir value dataframes
        p_df = self.p_value(df)
        rir_df = self.create_rir(df)
        combined_df = pd.concat([p_df, rir_df], axis=1)
        combined_df = combined_df.reindex(list(p_df.index))
        combined_df = combined_df.reset_index()
        combined_df.columns = ["Question", "P value", "Rir value", "positive"]
        
        # Create plot
        sns.set(style="darkgrid")
        fig, axes = plt.subplots(1, 2, figsize=(12, 7), sharey=True)
        plt.suptitle('P value and Rir value per question')
        
        # Plot the p value
        sns.barplot(
            x="P value", y="Question", data=combined_df, color='b',orient='h',order=list(p_df.index),
            ax=axes[0]).set_xlim(0, 1.0)
        
        # Plot the rir value
        #combined_df.plot.barh(x='Question', y='Rir value', xlim=(-1,1), ax=axes[1])
        sns.barplot(
            x="Rir value",
            y="Question",
            data=combined_df,
            orient='h',
            ax=axes[1],
            palette=combined_df["positive"]).set_xlim(-1.0, 1.0)

    def f(self, row):
        """Returns a color based on the rir value of the row"""
        if row['rir_value'] <= 0:
            return 'r'
        elif row['rir_value'] <= 0.25:
            return 'y'
        else:
            return 'g'

    def create_rir(self, df):
        rir_dict = {}

        if len(df["student_id"].unique()) < 50:
            print("Norm of 50 students not reached to be meaningful")

        df['student_score-item'] = df['score'].groupby(
            df['student_id']).transform('sum') - df['score']
        
        for question in sorted(set(df["question_name"].values)):
            temp_df = df.loc[df['question_name'] == question]
            rir_dict[question] = temp_df[[
                "score", "student_score-item"
            ]].corr().iloc[1, 0]
            
        rir_df = pd.DataFrame.from_dict(
            rir_dict, orient='index', columns=["rir_value"])
        rir_df['positive'] = rir_df.apply(self.f, axis=1)
        return rir_df

    def replace_with_resits(self, df, resit_name):
        """Replaces grades in a DataFrame with the corresponding resit"""
        assignments = self.resits[resit_name]
        if resit_name in df.columns:
            assert isinstance(assignments, list), "The value of the resit in workflow.json should be a list of assignments"
            for assignment in assignments:
                df[assignment] = np.where(
                    df[resit_name].isnull(), df[assignment], df[resit_name])
        return df

    def create_overview(self, df):
        # If there is no canvas course, use nbgrader
        # If there is a canvas course, combine nbgrader and canvas
        if self.canvas_course is None:
            if df is None:
                return None
            df.dropna(1, how='all', inplace=True)
            df = df.fillna(0)
        else:
            # Get grades from canvas
            canvas_df = self.create_canvas_grades_df()
            canvas_df.dropna(1, how='all', inplace=True)
#             if canvas_df.empty or canvas_df.sum().sum() == 0:
#                 return None

            # Add columns to canvas_df that are only in nbgrader columns
            for column in df.dropna(1, how='all').columns:
                if column not in canvas_df.columns:
                    canvas_df = canvas_df.join(
                        df[column].fillna(0), how='left')

            df = canvas_df
        order_of_assignments = [assignment for assignment in self.sequence if assignment in df.columns]
        list_of_categories = []

        for n, assignment in enumerate(order_of_assignments):
            
            # If assignment is resit, replace assignment with resit results
            if assignment in self.resits.keys():
                df = self.replace_with_resits(df, assignment)

            insuifficent = []
            for requirement in self.requirements:
                if isinstance(requirement['groups'], list):
                    assignments = set()
                    for group_name in requirement['groups']:
                        assignments |= set(
                            self.groups[group_name]['assignments'])
                    weighted_total = self.add_total_to_df(
                        df[assignments & set(order_of_assignments[:n + 1])])[0]

                    insuifficent += list(
                        weighted_total[weighted_total < requirement['min_grade']].index)

                else:
                    columns = set(
                        [x for x in order_of_assignments[:n + 1] if x in self.groups[requirement['groups']]['assignments']])
                    if columns != set():
                        insuifficent += list(df[df[columns].mean(axis=1)
                                                < requirement['min_grade']].index)

            weighted_total = self.add_total_to_df(df[order_of_assignments[:n + 1]])[0]
            insuifficent += list(weighted_total[weighted_total < 5.5].index)

            fail_counter = Counter(Counter(insuifficent).values())
            temp_df = df[df[assignment] > 0]
            did_not_participate = (set(df.index) -
                                   set(temp_df.index)) & set(insuifficent)
            fail_counter = Counter(
                Counter([x for x in insuifficent if x not in did_not_participate]).values())
            list_of_categories.append([assignment, len(df) - len(set(insuifficent))] + [fail_counter[x]
                                                                               for x in range(1, len(self.requirements) + 2,)] + [len(did_not_participate)])

        df = pd.DataFrame(
            list_of_categories,
            columns=[
                "Assignment Name",
                "Pass",
                "Insuifficient for 1 requirement"] +
            [
                "Insuifficient for %i requirements" %
                i for i in range(
                    2,
                    len(
                        self.requirements) +
                    2)] +
            ["Did not participate in this assignment &\n insuifficient for requirement(s)"]).set_index("Assignment Name")
        return df

    def visualize_overview(self):
        df = self.total_df()
        overviewdf = self.create_overview(df)
        if df is None:
            print("No grades available")
            return None

        fig, axes = plt.subplots(2, 1, figsize=(12, 12), sharex=True)
        sns.set(style="darkgrid")
        plt.suptitle('Overview of the course', y=0.93)
        df = df.reindex(
            [x for x in self.sequence if x in overviewdf.index], axis=1)
        a = sns.boxplot(data=df.mask(df < 1.0), ax=axes[0])
        a.set_title('Boxplot for each assignment')
        a.set_ylim(1, 10)
        sns.despine()
        flatui = sns.color_palette("Greens",
                                   1) + sns.color_palette("YlOrRd",
                                                          len(overviewdf.columns) - 2) + sns.color_palette("Greys",
                                                                                                           1)
        sns.set_palette(flatui)
        b = overviewdf.plot.bar(
            stacked=True,
            color=flatui,
            ylim=(0, overviewdf.sum(axis=1).max()),
            width=1.0,
            legend='reverse',
            ax=axes[1])
        b.set_title(
            'How many students have suifficient grades to pass after that assignment'
        )
        plt.xticks(rotation=45)
        plt.legend(
            loc='right',
            bbox_to_anchor=(1.4, 0.8),
            fancybox=True,
            shadow=True,
            ncol=1)

    def upload_button(self):
        if self.canvas_course is None:
            print(
                "Credentials for Canvas were not provided, therefore it is not possible to upload.")
            return
        canvas_button = interact_manual.options(
            manual_name="Grades to Canvas")
        canvas_button(
            self.upload_to_canvas,
            assignment_name=self.canvas_and_nbgrader())

    def upload_to_canvas(self, assignment_name, message='', feedback=False):
        # If chosen, create feedback files
        if feedback:
            print("Creating feedbackfiles")
            subprocess.run([
                "nbgrader", "feedback", "--quiet", "--force",
                "--assignment=%s" % assignment_name
            ])
            print("Feedbackfiles created")

        # Get the latest grades from the gradebook
        canvasdf = self.total_df()
        student_dict = self.get_student_ids()

        assignment = self.get_assignment_obj(assignment_name)
                          
        # Check if assignment is published on Canvas, otherwise publish
        if not assignment.published:
            assignment.edit(assignment={"published": True})
                          
        # loop over alle submissions voor een assignment, alleen als er
        # attachments zijn
        for submission in tqdm_notebook(
                assignment.get_submissions(), desc='Submissions', leave=False):
            try:
                student_id = student_dict[submission.user_id]
            except Exception as e:
                continue
            if student_id not in list(canvasdf.index.values):
                continue
            grade = canvasdf.at[student_id, assignment_name]
            if np.isnan(grade):
                continue
            grade_on_canvas = submission.attributes['score'] if submission.attributes['score']!=None else -1
                                          
            # Only changes grades when grade on canvas is lower
            if grade_on_canvas < grade and grade_on_canvas != 0:
                
                if feedback:
                    if os.path.exists(
                        'feedback/%s/%s/%s.html' %
                            (student_id, assignment_name, assignment_name)):
                        feedbackfile = self.create_feedback(
                            student_id, assignment_name)
                        submission.upload_comment(feedbackfile)
                    else:
                        print(
                            "No feedbackfile found for student %s" %
                            student_id)
                submission.edit(
                    submission={'posted_grade': str(grade)},
                    comment={'text_comment': message})

        # Delete feedbackfiles to save memory
        if 'canvasfeedback' in os.listdir():
            shutil.rmtree('canvasfeedback/', ignore_errors=True)
        if 'feedback' in os.listdir():
            shutil.rmtree('feedback/', ignore_errors=True)

    def get_student_ids(self):
        return {
            student.id: student.sis_user_id
            for student in self.canvas_course.get_users()
        }

    def visualize_validity(self):
        canvas_grades = self.total_df()
                          
        if canvas_grades is None:
            print("No grades available")
            return
                          
        cronbach_df = self.cronbach_alpha_plot()
        fig, axes = plt.subplots(1, 2, figsize=(15, 7))
        sns.set(style="darkgrid")
        correlation_plot = sns.heatmap(
            canvas_grades.corr(),
            vmin=-1,
            vmax=1.0,
            annot=True,
            linewidths=.5,
            cmap="RdYlGn",
            ax=axes[0])
        correlation_plot.set_title("Correlations between assignments")
        correlation_plot.set(ylabel='', xlabel='')

        cronbachplot = sns.barplot(
            y="Assignment",
            x="Cronbachs Alpha",
            data=cronbach_df,
            palette=map(self.color_ca_plot, cronbach_df["Cronbachs Alpha"]),
            ax=axes[1])
        cronbachplot.set_xlim(0, 1.0)
        cronbachplot.set(ylabel='')
        cronbachplot.set_title("Cronbachs Alpha for each assignment")

    def create_feedback(self, student_id, assignment_id):
        """Given a student_id and assignment_id, creates a feedback file without the Hidden Tests"""
        directory = 'feedback/%s/%s/' % (student_id, assignment_id)
        soup = str(
            BeautifulSoup(
                open(
                    "%s%s.html" % (directory, assignment_id),
                    encoding='utf-8'), "html.parser"))
        css, html = soup.split('</head>', 1)
        html = re.sub(
            r'(<div class="output_subarea output_text output_error">\n<pre>\n)(?:(?!<\/div>)[\w\W])*(<span class=".*?">.*?Error)',
            r'\1\2',
            html)
        html = re.sub(
            r'<span class="c1">### BEGIN HIDDEN TESTS<\/span>[\w\W]*?<span class="c1">### END HIDDEN TESTS<\/span>',
            '',
            html)
        soup = css + '</head>' + html
        targetdirectory = 'canvasfeedback/%s/%s/' % (student_id, assignment_id)
        if not os.path.exists(targetdirectory):
            os.makedirs(targetdirectory)
        filename = "%s%s.html" % (targetdirectory, assignment_id)
        Html_file = open(filename, "w", encoding="utf8")
        Html_file.write(soup)
        Html_file.close()
        return filename

    def color_ca_plot(self, c):
        pal = sns.color_palette("RdYlGn_r", 6)
        if c >= 0.8:
            return pal[0]
        elif c >= 0.6:
            return pal[1]
        else:
            return pal[5]

    def cronbach_alpha_plot(self):
        """Returns a dataframe with the Cronbachs Alpha per assignment""" 

        df = pd.pivot_table(
            self.create_results_per_question(),
            values='score',
            index=['student_id'],
            columns=['assignment', 'question_name'],
            aggfunc=np.sum)
        cronbach_list = []
        for assignment_id in sorted(set(df.columns.get_level_values(0))):
            items = df[assignment_id].dropna(how='all').fillna(0)

            # source:
            # https://github.com/anthropedia/tci-stats/blob/master/tcistats/__init__.py
            items_count = items.shape[1]
            variance_sum = float(items.var(axis=0, ddof=1).sum())
            total_var = float(items.sum(axis=1).var(ddof=1))

            cronbach_list.append((assignment_id,
                                  (items_count / float(items_count - 1) *
                                   (1 - variance_sum / total_var))))

        cronbach_df = pd.DataFrame(
            cronbach_list, columns=["Assignment", "Cronbachs Alpha"])
        return cronbach_df

    def canvas_and_nbgrader(self):
        """Returns a list of assignments that are both in canvas and in nbgrader"""
        canvas = set(assignment.name
                     for assignment in self.canvas_course.get_assignments())
        nbgrader = set(
            assignment
            for assignment in self.nbgrader_api.get_source_assignments())
        return sorted(canvas & nbgrader)

    def TurnToUvaScores(self, grade):
        # 5.5 can't exist
        if grade > 5 and grade < 6:
            return round(grade)

        # Because rounding is weird in python
        # https://stackoverflow.com/questions/14249971/why-is-pythons-round-so-strange
        elif int(2 * grade) % 2 == 0:
            return 0.5 * (round(2 * grade + 1) - 1)
        else:
            return 0.5 * round(2 * grade)

    def NAV(self, row, dict_of_weights):
        if row['Total'] < 5.5:
            return "NAV"

        for requirement in self.requirements:
            if isinstance(requirement['groups'], list):
                total_weight = sum([dict_of_weights[group]
                                    for group in requirement['groups']])
                total = sum([row[group] * dict_of_weights[group]
                             for group in requirement['groups']])
                if total / total_weight < requirement['min_grade']:
                    return "NAV"
            else:
                if requirement['groups'] in row.index:
                    if row[requirement['groups']] < requirement['min_grade']:
                        return "NAV"

        return row['Total']

    def add_total_to_df(self, df):
        dict_of_weights = {}
        assignment_dict = [l for l in self.canvas_course.get_assignments()]
        for group_name, d in self.groups.items():
            if len(set(d['assignments']) & set(df.columns)) > 0:
                dict_of_weights[group_name] = d['weight']
                assignments = [
                    l.name for l in assignment_dict
                    if l.name in d['assignments']
                ]
                df[group_name] = df[set(df.columns) & set(
                    assignments)].fillna(0).mean(axis=1)

        dict_of_weights = {
            x: y / sum(dict_of_weights.values())
            for x, y in dict_of_weights.items()}
        df['Total'] = 0
        for k, v in dict_of_weights.items():
            df['Total'] += df[k] * v
        return df['Total'], dict_of_weights

    def create_canvas_grades_df(self):
        student_dict = self.get_student_ids()

        assignment_list = [l for l in self.canvas_course.get_assignments()]
        dict_of_grades = {
            i.name: {
                student_dict[j.user_id]: j.grade
                for j in i.get_submissions() if j.user_id in student_dict
            }
            for i in assignment_list
        }

        return pd.DataFrame.from_dict(
            dict_of_grades, orient='columns').astype(float)

    def final_grades(self):
        if self.canvas_course is None:
            print("This function only works with Canvas.")
            return
        df = self.create_canvas_grades_df()
        
        if df.empty:
            print("No grades available")
            return
        resits = [
            assignment for assignment in self.sequence if assignment in self.resits.keys()]
        for resit in resits:
            df = self.replace_with_resits(df, resit)
        df.dropna(1, how='all', inplace=True)

        df['Total'], dict_of_weights = self.add_total_to_df(df)

        df["Total"] = df["Total"].map(self.TurnToUvaScores)
        df["TotaalNAV"] = df.apply(
            lambda row: self.NAV(
                row, dict_of_weights), axis=1)
        df["TotaalNAV"].reset_index().to_csv(
            'final_grades.csv', header=[
                "Student", "Final_grade"], index=False)
        df["cat"] = df['TotaalNAV'] != 'NAV'
        df["Passed"] = np.where(df.cat, df['Total'], np.nan)
        df["Failed"] = np.where(df.cat, np.nan, df['Total'])
        
        # Plot histogram of final grades
        ax = df[["Passed", "Failed"]].plot.hist(
            bins=np.arange(-0.25, 10.5, 0.5), color=['green', 'red'], title="Final grades")
        ax.set_xlim(xmin=0, xmax=10)
        ax.set_xticks(np.arange(0, 10.5, 1))
        print("Grades have been exported to final_grades.csv")

        # Only allow uploading final grades if all assignments have been graded
        if set(self.canvas_and_nbgrader()).issuperset(set(itertools.chain.from_iterable(
                v["assignments"] for k, v in self.groups.items() if v["weight"] > 0))):
            final_grades_button = interact_manual.options(
                manual_name="Upload final grades")
            final_grades_button(
                self.upload_final_grades,
                column="", totalnav=fixed(df["TotaalNAV"]))

    def upload_final_grades(self, column, totalnav):
        """Uploads the final grades to canvas column"""
        assignmentdict = {
            assignment.name: assignment.id
            for assignment in self.canvas_course.get_assignments()
        }

        # If column for final grade does not exist, create
        if column not in assignmentdict.keys():
            self.canvas_course.create_assignment(
                assignment={
                    'name': column,
                    'points_possible': 10,
                    'submission_types': 'online_upload',
                    'published': 'True',
                    'omit_from_final_grade': True
                })

        student_dict = self.get_student_ids()
        assignment = self.get_assignment_obj(column)
                                          
        # Check if assignment is published on Canvas, otherwise publish
        if not assignment.published:
            assignment.edit(assignment={"published": True})
                                          
        for submission in tqdm_notebook(
                assignment.get_submissions(), desc='Students', leave=False):
            try:
                student_id = student_dict[submission.user_id]
            except Exception as e:
                continue
            if student_id not in list(totalnav.index.values):
                continue
            grade = totalnav.at[student_id]
            if grade == "NAV":
                grade = 0
            if not np.isnan(grade):
                submission.edit(submission={'posted_grade': str(grade)})
