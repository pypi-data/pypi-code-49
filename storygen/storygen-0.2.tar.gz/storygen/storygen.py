import math
from collections import defaultdict, OrderedDict
import inflect


class Story:
    def __init__(self, student_obj, args):
        self.choices = args

        self.p = inflect.engine()

        self.data = student_obj
        self.semesters_list = self.data['semesters']
        (
            self.course_work,
            self.core_course_work,
            self.lowest_grade,
            self.summer_semesters_count,
            self.passed_credits_count,
            self.passed_credits,
            self.withdrawn_credits_count,
            self.withdrawn_credits,
            self.attempted_credits,
            self.failed_credits_count,
            self.failed_credits,
            self.d_credits_count,
            self.d_scored_credits,
            self.transferred_courses_count,
            self.transferred_courses,
            self.good_standing_sem_count,
            self.probation_sem_count,
            self.suspended_academic_count,
            self.advisor_count
        ) = self.get_course_work()

        (self.first_semester_adv, self.first_advisor_period) = self.get_advisor_first_semester()
        #         (self.advisors_count, self.first_advisor_semester) = self.get_advisors_info()
        (self.age_admitted, self.primary_ethnicity, self.gender, self.current_age) = self.get_demographic_data()
        self.student_name = self.data["name"]
        (self.pronoun, self.pronoun_2, self.pronoun_3) = self.get_pronouns()
        self.major = self.get_major()
        self.enrollment_date = self.get_enrollment_date()
        self.semester_count = len(self.semesters_list) - self.summer_semesters_count
        self.expected_grad_date = self.get_expected_grad()
        (self.grad_ind, self.graduation_date, self.last_semester_enrolled) = self.get_garduation_status()
        (self.gpa_ind, self.graduation_gpa) = self.get_gpa()
#         self.last_sem_enrolled = self.get_last_sem_enrolled()
        (self.failed_course, self.semester_failed_course, self.new_grade_f,
         self.semester_passed_course_f) = self.get_failed_then_passed()
        (self.withdrawn_course, self.semester_withdrawn_course, self.new_grade_w,
         self.semester_passed_course_w) = self.get_withdrawn_then_passed()

        #         USER SELECTION WORK
        self.citizenship_desc = (self.data['background']['demographics']['citizenship_desc'] if type(
            self.data['background']['demographics']['citizenship_desc']) == str else "")
        if self.citizenship_desc == "United States Citizen": self.citizenship_desc = "United States"
        self.citizenship_type = (self.data['background']['demographics']['citizenship_type'] if type(
            self.data['background']['demographics']['citizenship_type']) == str else "")
        self.current_age = (self.data['background']['demographics']['current_age'] if type(
            self.data['background']['demographics']['current_age']) == str else "")
        self.gender_desc = (self.data['background']['demographics']['gender_desc'] if type(
            self.data['background']['demographics']['gender_desc']) == str else "")
        self.nation_of_citizenship_desc = (
            self.data['background']['demographics']['nation_of_citizenship_desc'] if type(
                self.data['background']['demographics']['nation_of_citizenship_desc']) == str else "")
        self.primary_ethnicity_desc = (self.data['background']['demographics']['primary_ethnicity_desc'] if type(
            self.data['background']['demographics']['primary_ethnicity_desc']) == str else "")
        self.admission_population = self.get_admission_population()
        self.recent_gpa = self.get_recent_gpa()

        # CREATING STORY TEXTUAL CONTENT
        self.dem_text = self.get_dem_text()
        self.trans_text = self.get_trans_text()
        self.d_credits_text = self.get_d_credits_text()
        self.lowest_text = self.get_lowest_text()
        self.failed_then_passed_text = self.get_failed_then_passed_text()
        self.grad_text = self.get_grad_text()

        # DYNAMIC WORK
        self.credits_text = self.get_credits_text()

        self.temporal_story = []
        self.outcome_story = []
        self.default_story = []
        
        self.default_story.append({"docs": self.dem_text, "segment_name": "demo_text"})
        self.default_story.append({"docs": self.trans_text, "segment_name": "trans_text"})
        self.default_story.append({"docs": self.d_credits_text, "segment_name": "d_credits_text"})
        self.default_story.append({"docs": self.lowest_text, "segment_name": "lowest_text"})
        self.default_story.append({"docs": self.failed_then_passed_text, "segment_name": "failed_then_passed"})
        self.default_story.append({"docs": self.grad_text, "segment_name": "grad_text"})

        self.temporal_story = self.get_temporal_story()
        self.outcome_story = self.get_outcome_story()
    
    def get_last_sem_enrolled(self):
        def get_date(date):
            date = str(date)
            semester_names = {
                1: "Spring",
                5: "First Summer",
                7: "Second Summer",
                8: "Fall"
            }
            return semester_names[int(date[4:5])] + str(date[:4])
        try:
            return get_date(self.data['grad_info']['last_semester_enrolled'])
        except:
            return ''
    
    def get_academic_standing_text(self):
        good_standing_sem_text = []
        probation_sem_text = []
        suspended_academic_text = []

        if self.good_standing_sem_count > 0:
            if self.good_standing_sem_count == 1:
                good_standing_sem_text = [
                    self.create_text(" in good academic standing for ", "template", None),
                    self.create_text(self.p.number_to_words(self.good_standing_sem_count), "dynamic",
                                     "academic_standing_desc"),
                    self.create_text(" semester", "template", None),
                ]
            else:
                good_standing_sem_text = [
                    self.create_text(" in good academic standing for ", "template", None),
                    self.create_text(self.p.number_to_words(self.good_standing_sem_count), "dynamic",
                                     "academic_standing_desc"),
                    self.create_text(" semesters", "template", None),
                ]
        if self.probation_sem_count > 0:
            if self.probation_sem_count == 1:
                probation_sem_text = [
                    self.create_text(" on probation for ", "template", None),
                    self.create_text(self.p.number_to_words(self.probation_sem_count), "dynamic",
                                     "academic_standing_desc"),
                    self.create_text(" semester", "template", None),
                ]
            else:
                probation_sem_text = [
                    self.create_text(" on probation for ", "template", None),
                    self.create_text(self.p.number_to_words(self.probation_sem_count), "dynamic",
                                     "academic_standing_desc"),
                    self.create_text(" semesters", "template", None),
                ]
        if self.suspended_academic_count > 0:
            if self.suspended_academic_count == 1:
                suspended_academic_text = [
                    self.create_text(" suspended for ", "template", None),
                    self.create_text(self.p.number_to_words(self.suspended_academic_count), "dynamic",
                                     "academic_standing_desc"),
                    self.create_text(" semester", "template", None),
                ]
            else:
                suspended_academic_text = [
                    self.create_text(" suspended for ", "template", None),
                    self.create_text(self.p.number_to_words(self.suspended_academic_count), "dynamic",
                                     "academic_standing_desc"),
                    self.create_text(" semesters", "template", None),
                ]

        comma_text = [self.create_text(",", "template", None)]
        dot_text = [self.create_text(". ", "template", None)]
        and_text = [self.create_text(" and", "template", None)]
        academic_standing_text = [
            self.create_text("During ", "template", None),
            self.create_text(self.pronoun_2, "dynamic", "gender"),
            self.create_text(" enrollment, ", "template", None),
            self.create_text(self.student_name, "template", "name"),
            self.create_text(" was", "template", None),
        ]

        if self.good_standing_sem_count > 0 and self.probation_sem_count == 0 and self.suspended_academic_count == 0:
            academic_standing_text = academic_standing_text + good_standing_sem_text + dot_text
        elif self.good_standing_sem_count > 0 and self.probation_sem_count > 0 and self.suspended_academic_count == 0:
            academic_standing_text = academic_standing_text + good_standing_sem_text + and_text + probation_sem_text + dot_text
        elif self.good_standing_sem_count > 0 and self.probation_sem_count == 0 and self.suspended_academic_count > 0:
            academic_standing_text = academic_standing_text + good_standing_sem_text + and_text + suspended_academic_text + dot_text
        elif self.good_standing_sem_count > 0 and self.probation_sem_count > 0 and self.suspended_academic_count > 0:
            academic_standing_text = academic_standing_text + good_standing_sem_text + comma_text + probation_sem_text + and_text + suspended_academic_text + dot_text
        elif self.good_standing_sem_count == 0 and self.probation_sem_count > 0 and self.suspended_academic_count == 0:
            academic_standing_text = academic_standing_text + probation_sem_text + dot_text
        elif self.good_standing_sem_count == 0 and self.probation_sem_count > 0 and self.suspended_academic_count > 0:
            academic_standing_text = academic_standing_text + probation_sem_text + and_text + suspended_academic_text + dot_text
        elif self.good_standing_sem_count == 0 and self.probation_sem_count == 0 and self.suspended_academic_count > 0:
            academic_standing_text = academic_standing_text + suspended_academic_text + dot_text
        else:
            academic_standing_text = [self.create_text("", "template", None)]

        return academic_standing_text

    def get_adv_text(self):
        adv_text = [self.create_text("", "template", None)]
        if self.advisor_count == 0:
            adv_text = [
                self.create_text(self.pronoun, "dynamic", "gender"),
                self.create_text(" had never assigned an advisor throughout ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" enrollment. ", "template", None),
            ]
        elif self.advisor_count == 1:
            adv_text = [
                self.create_text(self.pronoun, "dynamic", "gender"),
                self.create_text(" had only ", "template", None),
                self.create_text("one", "dynamic", "advisor_count"),
                self.create_text(" advisor throughout ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" enrollment. ", "template", None),
            ]
        else:
            adv_text = [
                self.create_text("Throughout ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender_desc"),
                self.create_text(" enrollment, ", "template", None),
                self.create_text(self.student_name, "dynamic", "student_name"),
                self.create_text(" has ", "template", None),
                self.create_text(self.p.number_to_words(self.advisor_count), "dynamic", "advisor_count"),
                self.create_text(" advisors and ", "template", None),
                self.create_text(self.pronoun.lower(), "dynamic", "gender_desc"),
                self.create_text(" had assigned ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender_desc"),
                self.create_text(" first advisor in ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender_desc"),
                self.create_text(" ", "template", None),
                self.create_text(self.first_semester_adv, "dynamic", "advisor_count"),
                self.create_text(" semester in ", "template", None),
                self.create_text(self.first_advisor_period, "dynamic", "advisor_count"),
                self.create_text(". ", "template", None)
            ]
        return adv_text

    def get_temporal_story(self):
        #         Initialize all here!
        temporal_story = []
        academic_standing_text = [self.create_text("", "template", None)]
        adv_text = [self.create_text("", "template", None)]
        credits_text = [self.create_text("", "template", None)]
        specific_dem_text = [self.create_text("", "template", None)]

        academic_standing_text = self.get_academic_standing_text()
        if self.choices[7] == '1':
            adv_text = self.get_adv_text()
        specific_dem_text = self.get_specific_dem_text()

        if '1' in [self.choices[9], self.choices[10]]:
            credits_text = self.credits_text

        temporal_story.append({"docs": specific_dem_text, "segment_name": "specific_demo_text"})
        temporal_story.append({"docs": self.trans_text, "segment_name": "trans_text"})
        temporal_story.append({"docs": self.credits_text, "segment_name": "credits_text"})
        temporal_story.append({"docs": self.d_credits_text, "segment_name": "d_credits_text"})
        temporal_story.append({"docs": adv_text, "segment_name": "adv_text"})
        temporal_story.append({"docs": self.lowest_text, "segment_name": "lowest_text"})
        temporal_story.append({"docs": self.failed_then_passed_text, "segment_name": "failed_then_passed"})
        temporal_story.append({"docs": academic_standing_text, "segment_name": "academic_standing_text"})
        temporal_story.append({"docs": self.grad_text, "segment_name": "grad_text"})
        return temporal_story

    def get_outcome_story(self):
        outcome_story = []
        outcome_intro_text = [self.create_text("", "template", None)]
        adv_text = [self.create_text("", "template", None)]
        credits_text = [self.create_text("", "template", None)]
        specific_dem_text = [self.create_text("", "template", None)]

        academic_standing_text = self.get_academic_standing_text()
        if self.choices[7] == '1':
            adv_text = self.get_adv_text()
        specific_dem_text = self.get_specific_dem_text()

        if '1' in [self.choices[9], self.choices[10]]:
            credits_text = self.credits_text

        if self.grad_ind == False and self.expected_grad_date != "" and self.last_semester_enrolled != "":
            outcome_intro_text = [
                self.create_text(self.student_name, "dynamic", "student_name"),
                self.create_text(" is a ", "template", None),
                self.create_text(self.gender, "dynamic", "gender"),
                self.create_text(" student who did not graduate yet and ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" last semester enrolled was ", "template", None),
                self.create_text(self.last_semester_enrolled, "dynamic", "last_semester_enrolled"),
                self.create_text(", while ", "template", None),
                self.create_text(self.pronoun, "dynamic", "gender"),
                self.create_text(" was expected to graduate in ", "template", None),
                self.create_text(self.expected_grad_date, "dynamic", "expected_grad_date"),
                self.create_text(". ", "template", None),
            ]
            if self.choices[8] == '1' and str(self.recent_gpa) != 'nan':
                outcome_intro_text += [
                    self.create_text(self.pronoun_2.title(), "dynamic", "gender"),
                    self.create_text(" most recent GPA is ", "template", None),
                    self.create_text(str(self.recent_gpa), "dynamic", "CGPA"),
                    self.create_text(". ", "template", None),
                ]
        elif self.grad_ind == False and self.expected_grad_date == "" and self.last_semester_enrolled == "":
            outcome_intro_text = [
                self.create_text(self.student_name, "dynamic", "student_name"),
                self.create_text(" is a ", "template", None),
                self.create_text(self.gender, "dynamic", "gender"),
                self.create_text(" student who did not graduate yet and there is no information about ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" expected graduation date nor last semester enrolled. ", "template", None),
            ]
            if self.choices[8] == '1' and str(self.recent_gpa) != 'nan':
                outcome_intro_text += [
                    self.create_text(self.pronoun_2.title(), "dynamic", "gender"),
                    self.create_text(" most recent GPA is ", "template", None),
                    self.create_text(str(self.recent_gpa), "dynamic", "CGPA"),
                    self.create_text(". ", "template", None),
                ]
        elif self.grad_ind == False and self.expected_grad_date == "" and self.last_semester_enrolled != "":
            outcome_intro_text = [
                self.create_text(self.student_name, "dynamic", "student_name"),
                self.create_text(" is a ", "template", None),
                self.create_text(self.gender, "dynamic", "gender"),
                self.create_text(" student who did not graduate yet and there is no information about ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" expected graduation date and ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" last semester enrolled was ", "template", None),
                self.create_text(self.last_semester_enrolled, "dynamic", None),
                self.create_text(". ", "template", None),
            ]
            if self.choices[8] == '1' and str(self.recent_gpa) != 'nan':
                outcome_intro_text += [
                    self.create_text(self.pronoun_2.title(), "dynamic", "gender"),
                    self.create_text(" most recent GPA is ", "template", None),
                    self.create_text(str(self.recent_gpa), "dynamic", "CGPA"),
                    self.create_text(". ", "template", None),
                ]
        elif self.grad_ind == False and self.expected_grad_date != "" and self.last_semester_enrolled == "":
            outcome_intro_text = [
                self.create_text(self.student_name, "dynamic", "student_name"),
                self.create_text(" is a ", "template", None),
                self.create_text(self.gender, "dynamic", "gender"),
                self.create_text(" student who did not graduate yet and ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" last semester enrolled was ", "template", None),
                self.create_text(self.last_semester_enrolled, "dynamic", "last_semester_enrolled"),
                self.create_text(", while ", "template", None),
                self.create_text(self.pronoun, "dynamic", "gender"),
                self.create_text(" was expected to graduate in ", "template", None),
                self.create_text(self.expected_grad_date, "dynamic", "expected_grad_date"),
                self.create_text(". ", "template", None),
            ]
            if self.choices[8] == '1' and str(self.recent_gpa) != 'nan':
                outcome_intro_text += [
                    self.create_text(self.pronoun_2.title(), "dynamic", "gender"),
                    self.create_text(" most recent GPA is ", "template", None),
                    self.create_text(str(self.recent_gpa), "dynamic", "CGPA"),
                    self.create_text(". ", "template", None),
                ]
        elif self.grad_ind == True:
            outcome_intro_text = [
                self.create_text(self.student_name, "dynamic", "student_name"),
                self.create_text(" is a ", "template", None),
                self.create_text(self.gender, "dynamic", "gender"),
                self.create_text(" student who was graduated after ", "template", None),
                self.create_text(self.p.number_to_words(self.semester_count), "dynamic", "semester_count"),
                self.create_text(" semesters in ", "template", None),
                self.create_text(self.graduation_date, "dynamic", "graduation_date"),
                self.create_text(" with a GPA of ", "template", None),
                self.create_text(str(self.graduation_gpa), "dynamic", "graduation_gpa"),
                self.create_text(". ", "template", None),
            ]

        academic_standing_text = self.get_academic_standing_text()
        specific_intro_text = self.get_specific_intro_text()

        outcome_story.append({"docs": outcome_intro_text, "segment_name": "outcome_intro_text"})
        outcome_story.append({"docs": specific_intro_text, "segment_name": "specific_intro_text"})
        outcome_story.append({"docs": academic_standing_text, "segment_name": "academic_standing_text"})
        outcome_story.append({"docs": self.trans_text, "segment_name": "trans_text"})
        outcome_story.append({"docs": self.credits_text, "segment_name": "credits_text"})
        outcome_story.append({"docs": self.d_credits_text, "segment_name": "d_credits_text"})
        outcome_story.append({"docs": adv_text, "segment_name": "adv_text"})
        outcome_story.append({"docs": self.lowest_text, "segment_name": "lowest_text"})
        outcome_story.append({"docs": self.failed_then_passed_text, "segment_name": "failed_then_passed"})
        return outcome_story

    def get_advisor_first_semester(self):
        def suffix(d):
            return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')

        first_semester_adv = 1000
        for index, sem in enumerate(self.data['semesters'], 1):
            try:
                if sem['semesterInfo']['advisor_count'] > 0.0:
                    return (str(index) + suffix(index), sem['semesterInfo']['academic_period_desc'])
            except:
                return ("", "")
        return ("", "")

    def get_recent_gpa(self):
        return round(self.data['semesters'][-1]['semesterInfo']['CGPA'], 2)

    def get_course_work(self):
        course_work = defaultdict(list)
        core_course_work = defaultdict(list)
        lowest_grade = ''
        # Summer semesters count
        summer_semesters_set = set()
        semesters_names = set()
        summer_semesters_count = 0
        # Outcome found!
        found_outcome = (False if self.data['outcome'] == None else True)
        # Attempted credits
        attempted_credits = 0.0
        if found_outcome:
            attempted_credits = self.data['outcome']['credits_attempted']
        # Passed credits
        passed_credits_count = 0.0
        passed_credits = set()
        if found_outcome:
            passed_credits_count = self.data['outcome']['credits_passed']
        # Withdrawn credits
        withdrawn_credits_count = 0.0
        withdrawn_credits = set()
        # Failed credits
        failed_credits_count = 0.0
        failed_credits = set()
        # D scored credits
        d_credits_count = 0.0
        d_credits = set()
        # Transferred credits
        transferred_courses_count = 0.0
        transferred_courses = set()
        if found_outcome:
            transferred_courses_count = self.data['outcome']['transfer_credits_passed']
        # Academic standing
        academic_standing = []
        good_standing_sem_count = 0
        probation_sem_count = 0
        suspended_academic_count = 0
        # Advisor count
        advisor_count = 0.0

        for index, sem in enumerate(self.data['semesters'], 1):
            try:
                if sem['semesterInfo']['advisor_count'] > advisor_count:
                    advisor_count = sem['semesterInfo']['advisor_count']
            except:
                pass
            # Getting academic standings
            try:
                academic_standing.append(sem['semesterInfo']['academic_standing_desc'])
            except:
                pass
            # This line for finding number of summer semesters
            semesters_names.add(sem['courses'][0]['academic_period_desc'])
            if 'summer' in sem['courses'][0]['academic_period_desc'].lower():
                summer_semesters_set.add(sem['courses'][0]['academic_period_desc'])
            for course in sem['courses']:
                # Getting all course work
                course_work[course['course_title_short']].append(
                    (course['academic_period_desc'], course['final_grade']))
                # Getting core courses work
                if course['course_identification'] in ["ITCS1212", "ITSC1212", "ITCS1213", "ITSC1213", "ITCS2214",
                                                       "ITSC2214", "ITCS2175", "ITSC2175"]:
                    core_course_work[course['course_identification']].append(
                        (course['academic_period_desc'], course['final_grade']))
                # Getting lowest grade
                if course['transfer_course_ind'] == "N" and course['final_grade'] in ['A', 'B', 'C', 'D', 'F']:
                    if course['final_grade'] > lowest_grade:
                        lowest_grade = course['final_grade']
                # Getting attempted credits
                if not found_outcome:
                    if course['transfer_course_ind'] == 'N':
                        if math.isnan(course['credits_attempted']) == False:
                            attempted_credits = attempted_credits + course['credits_attempted']
                # Getting passed credits and count
                if not found_outcome:
                    if course['transfer_course_ind'] == 'N':
                        if math.isnan(course['credits_passed']) == False:
                            passed_credits_count = passed_credits_count + course['credits_passed']
                            passed_credits.add(course['course_title_short'].title())
                # Getting withdrawn credits and count
                if course['transfer_course_ind'] == 'N' and course['final_grade'] == 'W':
                    withdrawn_credits_count = withdrawn_credits_count + course['credits_attempted']
                    withdrawn_credits.add(course['course_title_short'].title())
                # Getting failed credits and count
                if course['course_failed_ind'] == "Y" and course['transfer_course_ind'] == "N":
                    if math.isnan(course['credits_attempted']) == False:
                        failed_credits_count = failed_credits_count + course['credits_attempted']
                        failed_credits.add(course['course_title_short'].title())
                # Getting D-scored credits
                if course['transfer_course_ind'] == 'N' and course['final_grade'] == 'D':
                    d_credits_count = d_credits_count + course['credits_attempted']
                    d_credits.add(course['course_title_short'].title())
                # Getting transferred credits and count
                if course['transfer_course_ind'] == "Y":
                    if math.isnan(course['credits_attempted']) == False:
                        transferred_courses_count = transferred_courses_count + course['credits_attempted']
                        try:
                            transferred_courses.add(course['course_title_short'].title())
                        except Exception as e:
                            pass
        # Getting number of summer semesters
        summer_semesters_count = len(summer_semesters_set)
        # Joining withdrawn credits
        withdrawn_credits = ", ".join(withdrawn_credits)
        # Joining failed credits
        failed_credits = ", ".join(failed_credits)
        # Joining D-scored credits
        d_credits = ", ".join(d_credits)
        # Joining transferred credits
        transferred_courses = ", ".join(transferred_courses)
        # Seperating academic standings
        good_standing_sem_count = academic_standing.count('Good Standing')
        probation_sem_count = academic_standing.count('Continued Probation') + academic_standing.count('Probation')
        suspended_academic_count = academic_standing.count('Suspended-Academic') + academic_standing.count(
            'Suspended-Academic-Reinstated')

        return (
            course_work,
            core_course_work,
            lowest_grade,
            summer_semesters_count,
            int(passed_credits_count),
            passed_credits,
            int(withdrawn_credits_count),
            withdrawn_credits,
            int(attempted_credits),
            int(failed_credits_count),
            failed_credits,
            int(d_credits_count),
            d_credits,
            int(transferred_courses_count),
            transferred_courses,
            good_standing_sem_count,
            probation_sem_count,
            suspended_academic_count,
            int(advisor_count)
        )

    def get_withdrawn_then_passed(self):
        for course, grade_list in self.course_work.items():
            if len(grade_list) > 1:
                if grade_list[0][1] == 'W' and grade_list[1][1] == 'A':
                    return (course, grade_list[0][0], 'an ' + grade_list[1][1], grade_list[1][0])
                elif grade_list[0][1] == 'W' and grade_list[1][1] == 'B':
                    return (course, grade_list[0][0], 'a ' + grade_list[1][1], grade_list[1][0])
        return ('', '', '', '')

    def get_failed_then_passed(self):
        for course, grade_list in self.course_work.items():
            if len(grade_list) > 1:
                if grade_list[0][1] == 'F' and grade_list[1][1] == 'A':
                    return (course, grade_list[0][0], 'an ' + grade_list[1][1], grade_list[1][0])
                elif grade_list[0][1] == 'F' and grade_list[1][1] == 'B':
                    return (course, grade_list[0][0], 'a ' + grade_list[1][1], grade_list[1][0])
        return ('', '', '', '')

    def get_demographic_data(self):
        temp_dict = self.data['background']['demographics']
        age_admitted = 0
        try:
            age_admitted = self.data['semesters'][0]['semesterInfo']['age_admitted']
        except:
            pass
        primary_ethnicity = (
            temp_dict['primary_ethnicity_desc'].lower() if type(temp_dict['primary_ethnicity_desc']) == str else '')
        gender = temp_dict['gender_desc'].lower()
        current_age = self.data["background"]["demographics"]['current_age']
        return (self.p.number_to_words(int(age_admitted)), primary_ethnicity, gender, current_age)

    def get_pronouns(self):
        return (("He", "his", "him") if self.data['background']['demographics']['gender_desc'] == "Male" else (
            "She", "her", "her"))

    def get_major(self):
        return self.data['semesters'][0]['semesterInfo']['major_desc']

    def get_admission_population(self):
        try:
            if 'Freshmen' in self.data['semesters'][0]['semesterInfo']['admissions_population_desc']:
                return 'freshman'
            elif 'Transfer' in self.data['semesters'][0]['semesterInfo']['admissions_population_desc']:
                return 'transfer'
            else:
                return ''
        except:
            return ''

    def get_enrollment_date(self):
        return self.data['semesters'][0]['courses'][0]['academic_period_desc']

    def get_expected_grad(self):
        def suffix(d):
            return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')

        def custom_strftime(format, t):
            return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

        try:
            date = self.data['semesters'][0]['semesterInfo']['expected_graduation_date']
            if len(date) > 9:
                year = int(date[:4])
                month = int(date[5:7])
                day = int(date[8:11])
                return custom_strftime('%B {S}, %Y', dt(year, month, day))
            else:
                return date
        except Exception as e:
            return ""

    def get_garduation_status(self):
        def suffix(d):
            return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')

        def custom_strftime(format, t):
            return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))
        
        def get_date(date):
            date = str(date)
            semester_names = {
                1: "Spring ",
                5: "First Summer ",
                7: "Second Summer ",
                8: "Fall "
            }
            return semester_names[int(date[4:5])] + str(date[:4])
            
            
        if self.data['grad_info']:
            if self.data['grad_info']['isGraduated'] == "Yes":
                return (True, get_date(self.data['grad_info']['last_semester_enrolled']), get_date(self.data['grad_info']['last_semester_enrolled']))
            elif self.data['grad_info']['isGraduated'] == "No":
                return (False, '', get_date(self.data['grad_info']['last_semester_enrolled']))
        elif self.data['outcome']:
            date = self.data['outcome']['outcome_graduation_date']
            if len(date) > 9:
                year = int(date[:4])
                month = int(date[5:7])
                day = int(date[8:11])
            return (True, custom_strftime('%B {S}, %Y', dt(year, month, day)), '')
        else:
            return (False, '', '')

    def get_gpa(self):
        if self.data['outcome'] == None:
            return (False, 0)
        else:
            return (True, round(self.data['latest_CGPA'], 2))

    def get_course_level(self):
        grad_level_count = 0.0
        u_grad_level_count = 0.0
        grad_level_courses = set()
        u_grad_level_courses = set()
        for k, v in self.semesters_list.items():
            for item in v:
                if item['transfer_course_ind'] == "N" and item['course_level_desc'] == "Graduate":
                    grad_level_count = grad_level_count + item['credits_attempted']
                    grad_level_courses.add(item['course_identification'])
                elif item['transfer_course_ind'] == "N" and item['course_level_desc'] == "Undergraduate":
                    u_grad_level_count = u_grad_level_count + item['credits_attempted']
                    u_grad_level_courses.add(item['course_identification'])
        return (int(grad_level_count), int(u_grad_level_count), grad_level_courses, u_grad_level_courses)

    def major_change(self):
        def suffix(d):
            return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')

        start_major_index = next(iter(sorted(self.data["semesters"]["academic_study"])))
        for item in self.data["semesters"]["academic_study"][start_major_index]:
            start_major = item["major_desc"]
            break
        for k, v in iter(sorted(self.data["semesters"]["academic_study"].items())):
            for item2 in v:
                if item2["major_desc"] != start_major:
                    return str(self.data["background"]["demographics"]["person_uid"]) + ": CHANGED MAJOR TO " + item2[
                        "major_desc"] + " FROM " + start_major + " in his/her " + str(k) + suffix(int(k)) + " semester"

    def create_text(self, text, tag, feature):
        return {
            "text": text,
            "tag": tag,
            "feature": feature,
        }

    def get_dem_text(self):
        dem_text = [self.create_text("", "template", None)]
        if self.age_admitted != 'zero':
            dem_text = [
                self.create_text(self.student_name, "dynamic", "student_name"),
                self.create_text(" is a ", "template", None),
                self.create_text(self.gender, "dynamic", "gender"),
                self.create_text(" student who was admitted at the age of ", "template", None),
                self.create_text(self.age_admitted, "dynamic", "age_admitted"),
                self.create_text(". ", "template", None),
                self.create_text(self.pronoun, "dynamic", "gender"),
                self.create_text(" was first enrolled in ", "template", None),
                self.create_text(self.enrollment_date, "dynamic", "enrollment_date"),
                self.create_text(" and started with a major in ", "template", None),
                self.create_text(self.major, "dynamic", "major"),
                self.create_text(". ", "template", None),
            ]
        else:
            dem_text = [
                self.create_text(self.student_name, "dynamic", "student_name"),
                self.create_text(" is a ", "template", None),
                self.create_text(self.gender, "dynamic", "gender"),
                self.create_text(" student who was first enrolled in ", "template", None),
                self.create_text(self.enrollment_date, "dynamic", "enrollment_date"),
                self.create_text(" and started with a major in ", "template", None),
                self.create_text(self.major, "dynamic", "major"),
                self.create_text(". ", "template", None),
            ]
        return dem_text

    def get_specific_dem_text(self):  # if admission_population in args
        specific_dem_text = [self.create_text("", "template", None)]
        if '1' in [self.choices[4], self.choices[5], self.choices[6]]:
            if self.admission_population != "" and self.age_admitted != 'zero':
                specific_dem_text = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.gender, "dynamic", "gender"),
                    self.create_text(" student who was admitted as a ", "template", None),
                    self.create_text(self.admission_population, "dynamic", "admissions_population_desc"),
                    self.create_text(" student at the age of ", "template", None),
                    self.create_text(self.age_admitted, "dynamic", "age_admitted"),
                    self.create_text(". ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" was first enrolled in ", "template", None),
                    self.create_text(self.enrollment_date, "dynamic", "enrollment_date"),
                    self.create_text(" and started with a major in ", "template", None),
                    self.create_text(self.major, "dynamic", "major"),
                    self.create_text(". ", "template", None),
                ]
            ###############################################################################################
            elif self.age_admitted != 'zero':
                specific_dem_text = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.gender, "dynamic", "gender"),
                    self.create_text(" student who was admitted at the age of ", "template", None),
                    self.create_text(self.age_admitted, "dynamic", "age_admitted"),
                    self.create_text(". ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" was first enrolled in ", "template", None),
                    self.create_text(self.enrollment_date, "dynamic", "enrollment_date"),
                    self.create_text(" and started with a major in ", "template", None),
                    self.create_text(self.major, "dynamic", "major"),
                    self.create_text(". ", "template", None),
                ]
            else:
                specific_dem_text = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.gender, "dynamic", "gender"),
                    self.create_text(" student who was first enrolled in ", "template", None),
                    self.create_text(self.enrollment_date, "dynamic", "enrollment_date"),
                    self.create_text(" and started with a major in ", "template", None),
                    self.create_text(self.major, "dynamic", "major"),
                    self.create_text(". ", "template", None),
                ]

        additional_dem_info = [self.create_text("", 'template', None)]
        if self.choices[3] == '1' and all(item == '0' for item in self.choices[0:3]):  # 0001
            if self.primary_ethnicity != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(". ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif self.choices[2] == '1' and self.choices[3] == '0' and all(
                item == '0' for item in self.choices[0:2]):  # 0010
            if self.current_age != "":
                additional_dem_info = [
                    self.create_text("Currently, ", "template", None),
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif self.choices[0] == '0' and self.choices[1] == '1' and all(
                item == '0' for item in self.choices[2:4]):  # 0100
            if self.nation_of_citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text("\'s nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif self.choices[0] == '1' and all(item == '0' for item in self.choices[1:4]):  # 1000
            if self.citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif self.choices[0] == '1' and self.choices[3] == '1' and all(
                item == '0' for item in self.choices[1:3]):  # 1001
            if self.primary_ethnicity != "" and self.citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(", ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            elif self.citizenship_desc == "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(". ", "template", None),
                ]
            elif self.primary_ethnicity == "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif self.choices[0] == '1' and self.choices[1] == '0' and self.choices[2] == '1' and self.choices[
            3] == '0':  # 1010
            if self.citizenship_desc != "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old now. ", "template", None),
                ]
            elif self.citizenship_desc == "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is now ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            elif self.current_age == "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif all(item == '1' for item in self.choices[0:2]) and all(item == '0' for item in self.choices[2:4]):  # 1100
            if self.citizenship_desc != "" and self.nation_of_citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.citizenship_desc == "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" \'s nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.nation_of_citizenship_desc == "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif all(item == '1' for item in self.choices[0:2]) and all(item == '0' for item in self.choices[2:4]):  # 1101
            if self.primary_ethnicity != "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(", ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.primary_ethnicity == "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.primary_ethnicity != "" and self.citizenship_desc == "" and self.nation_of_citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(" and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.primary_ethnicity != "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc == "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(", ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            elif self.primary_ethnicity != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text("student. ", "template", None),
                ]
            elif self.citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            elif self.nation_of_citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" \'s nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif all(item == '1' for item in self.choices[0:2]) and all(item == '0' for item in self.choices[2:4]):  # 1110
            if self.citizenship_desc != "" and self.nation_of_citizenship_desc != "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". Currently, ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),

                ]
            elif self.citizenship_desc == "" and self.nation_of_citizenship_desc != "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" \'s nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". Currently, ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),

                ]
            elif self.citizenship_desc != "" and self.nation_of_citizenship_desc == "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and currently ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),

                ]
            elif self.citizenship_desc != "" and self.nation_of_citizenship_desc != "" and self.current_age == "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            elif self.nation_of_citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" \'s nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old now. ", "template", None),

                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif all(item == '1' for item in self.choices[0:4]):  # 1111
            if self.primary_ethnicity != "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc != "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(", ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". Currently, ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            elif self.primary_ethnicity == "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc != "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". Currently, ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            elif self.primary_ethnicity != "" and self.citizenship_desc == "" and self.nation_of_citizenship_desc != "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(" student and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". Currently, ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            elif self.primary_ethnicity != "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc == "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(", ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and currently", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            elif self.primary_ethnicity != "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc != "" and self.current_age == "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(", ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.primary_ethnicity == "" and self.citizenship_desc == "" and self.nation_of_citizenship_desc != "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text("\'s nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". Currently, ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            elif self.primary_ethnicity == "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc == "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and currently ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            elif self.primary_ethnicity == "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc != "" and self.current_age == "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.primary_ethnicity != "" and self.citizenship_desc == "" and self.nation_of_citizenship_desc == "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(" student and currently ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            elif self.primary_ethnicity != "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc != "" and self.current_age == "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(", ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.primary_ethnicity != "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc == "" and self.current_age == "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(", ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            elif self.primary_ethnicity != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(" student. ", "template", None),
                ]
            elif self.citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            elif self.nation_of_citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.student_name, "dynamic", "student_name"),
                    self.create_text("\'s  nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.current_age != "":
                additional_dem_info = [
                    self.create_text(". Currently, ", "template", None),
                    self.create_text(self.student_name, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        specific_dem_text += additional_dem_info
        #         pprint(additional_dem_info)
        if all(item == '0' for item in self.choices[0:6]):
            specific_dem_text = self.dem_text
        print(specific_dem_text)
        return specific_dem_text

    def get_specific_intro_text(self):  # if admission_population in args
        specific_intro_text = [self.create_text("", "template", None)]
        if '1' in [self.choices[4], self.choices[5], self.choices[6]]:
            if self.admission_population != "" and self.age_admitted != 'zero':
                specific_intro_text = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" was admitted as a ", "template", None),
                    self.create_text(self.admission_population, "dynamic", "admissions_population_desc"),
                    self.create_text(" student at the age of ", "template", None),
                    self.create_text(self.age_admitted, "dynamic", "age_admitted"),
                    self.create_text(". ", "template", None),
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" was first enrolled in ", "template", None),
                    self.create_text(self.enrollment_date, "dynamic", "enrollment_date"),
                    self.create_text(" and started with a major in ", "template", None),
                    self.create_text(self.major, "dynamic", "major"),
                    self.create_text(". ", "template", None),
                ]
            ###############################################################################################
            elif self.age_admitted != 'zero':
                specific_intro_text = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" was admitted at the age of ", "template", None),
                    self.create_text(self.age_admitted, "dynamic", "age_admitted"),
                    self.create_text(". ", "template", None),
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" was first enrolled in ", "template", None),
                    self.create_text(self.enrollment_date, "dynamic", "enrollment_date"),
                    self.create_text(" and started with a major in ", "template", None),
                    self.create_text(self.major, "dynamic", "major"),
                    self.create_text(". ", "template", None),
                ]
            else:
                specific_intro_text = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" was first enrolled in ", "template", None),
                    self.create_text(self.enrollment_date, "dynamic", "enrollment_date"),
                    self.create_text(" and started with a major in ", "template", None),
                    self.create_text(self.major, "dynamic", "major"),
                    self.create_text(". ", "template", None),
                ]

        additional_dem_info = [self.create_text("", 'template', None)]
        if self.choices[3] == '1' and all(item == '0' for item in self.choices[0:3]):  # 0001
            if self.primary_ethnicity != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(". ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif self.choices[2] == '1' and self.choices[3] == '0' and all(
                item == '0' for item in self.choices[0:2]):  # 0010
            if self.current_age != "":
                additional_dem_info = [
                    self.create_text("Currently, ", "template", None),
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif self.choices[0] == '0' and self.choices[1] == '1' and all(
                item == '0' for item in self.choices[2:4]):  # 0100
            if self.nation_of_citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.pronoun_2.title(), "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif self.choices[0] == '1' and all(item == '0' for item in self.choices[1:4]):  # 1000
            if self.citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif self.choices[0] == '1' and self.choices[3] == '1' and all(
                item == '0' for item in self.choices[1:3]):  # 1001
            if self.primary_ethnicity != "" and self.citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(", ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            elif self.citizenship_desc == "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(". ", "template", None),
                ]
            elif self.primary_ethnicity == "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif self.choices[0] == '1' and self.choices[1] == '0' and self.choices[2] == '1' and self.choices[
            3] == '0':  # 1010
            if self.citizenship_desc != "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old now. ", "template", None),
                ]
            elif self.citizenship_desc == "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is now ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            elif self.current_age == "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif all(item == '1' for item in self.choices[0:2]) and all(item == '0' for item in self.choices[2:4]):  # 1100
            if self.citizenship_desc != "" and self.nation_of_citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.citizenship_desc == "":
                additional_dem_info = [
                    self.create_text(self.pronoun_2.title(), "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.nation_of_citizenship_desc == "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif all(item == '1' for item in self.choices[0:2]) and all(item == '0' for item in self.choices[2:4]):  # 1101
            if self.primary_ethnicity != "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(", ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.primary_ethnicity == "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.primary_ethnicity != "" and self.citizenship_desc == "" and self.nation_of_citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(" and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.primary_ethnicity != "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc == "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(", ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            elif self.primary_ethnicity != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text("student. ", "template", None),
                ]
            elif self.citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            elif self.nation_of_citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif all(item == '1' for item in self.choices[0:2]) and all(item == '0' for item in self.choices[2:4]):  # 1110
            if self.citizenship_desc != "" and self.nation_of_citizenship_desc != "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". Currently, ", "template", None),
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),

                ]
            elif self.citizenship_desc == "" and self.nation_of_citizenship_desc != "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.pronoun_2.title(), "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". Currently, ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),

                ]
            elif self.citizenship_desc != "" and self.nation_of_citizenship_desc == "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and currently ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),

                ]
            elif self.citizenship_desc != "" and self.nation_of_citizenship_desc != "" and self.current_age == "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            elif self.nation_of_citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old now. ", "template", None),

                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        elif all(item == '1' for item in self.choices[0:4]):  # 1111
            if self.primary_ethnicity != "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc != "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(", ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". Currently, ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            elif self.primary_ethnicity == "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc != "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". Currently, ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            elif self.primary_ethnicity != "" and self.citizenship_desc == "" and self.nation_of_citizenship_desc != "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(" student and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". Currently, ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            elif self.primary_ethnicity != "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc == "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(", ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and currently", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            elif self.primary_ethnicity != "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc != "" and self.current_age == "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(", ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.primary_ethnicity == "" and self.citizenship_desc == "" and self.nation_of_citizenship_desc != "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". Currently, ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            elif self.primary_ethnicity == "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc == "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and currently ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            elif self.primary_ethnicity == "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc != "" and self.current_age == "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.primary_ethnicity != "" and self.citizenship_desc == "" and self.nation_of_citizenship_desc == "" and self.current_age != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(" student and currently ", "template", None),
                    self.create_text(self.pronoun, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            elif self.primary_ethnicity != "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc != "" and self.current_age == "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(", ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen and ", "template", None),
                    self.create_text(self.pronoun_2, "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.primary_ethnicity != "" and self.citizenship_desc != "" and self.nation_of_citizenship_desc == "" and self.current_age == "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(", ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            elif self.primary_ethnicity != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.primary_ethnicity, "dynamic", "primary_ethnicity"),
                    self.create_text(" student. ", "template", None),
                ]
            elif self.citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.pronoun.title(), "dynamic", "gender"),
                    self.create_text(" is a ", "template", None),
                    self.create_text(self.citizenship_desc, "dynamic", "citizenship_desc"),
                    self.create_text(" citizen. ", "template", None),
                ]
            elif self.nation_of_citizenship_desc != "":
                additional_dem_info = [
                    self.create_text(self.pronoun_2.title(), "dynamic", "gender"),
                    self.create_text(" nation of citizenship is ", "template", None),
                    self.create_text(self.nation_of_citizenship_desc.title(), "dynamic", "nation_of_citizenship_desc"),
                    self.create_text(". ", "template", None),
                ]
            elif self.current_age != "":
                additional_dem_info = [
                    self.create_text("Currently, ", "template", None),
                    self.create_text(self.student_name, "dynamic", "gender"),
                    self.create_text(" is ", "template", None),
                    self.create_text(self.p.number_to_words(self.current_age), "dynamic", "current_age"),
                    self.create_text(" years old. ", "template", None),
                ]
            else:
                additional_dem_info = [self.create_text("", 'template', None)]
        specific_intro_text += additional_dem_info
        #         pprint(additional_dem_info)

        return specific_intro_text

    def get_trans_text(self):
        trans_text = [self.create_text("", "template", None)]
        if self.transferred_courses_count > 0:
            trans_text = [
                self.create_text(self.pronoun, "dynamic", "gender"),
                self.create_text(" transferred a total of ", "template", None),
                self.create_text(self.p.number_to_words(self.transferred_courses_count), "dynamic",
                                 "transferred_credits"),
                self.create_text(" credit hours from ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" previous school. ", "template", None),
            ]
        return trans_text

    def get_d_credits_text(self):
        d_credits_text = [self.create_text("", "template", None)]
        if self.d_credits_count > 0:
            d_credits_text = [
                self.create_text("Also, ", "template", None),
                self.create_text(self.pronoun.lower(), "dynamic", "gender"),
                self.create_text(" has scored D in a total of ", "template", None),
                self.create_text(self.p.number_to_words(self.d_credits_count), "dynamic", "final_grade"),
                self.create_text(" credit hours. ", "template", None),
            ]
        return d_credits_text

    def get_lowest_text(self):
        lowest_text = [self.create_text("", "template", None)]
        if self.lowest_grade == '':
            return lowest_text
        elif self.lowest_grade == 'F' or self.lowest_grade == 'D':
            return lowest_text 
        elif self.lowest_grade != 'A':
            lowest_text = [
                self.create_text("Throughout ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" enrollment in this major, ", "template", None),
                self.create_text(self.pronoun.lower(), "dynamic", "gender"),
                self.create_text(" maintained all ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" grades at ", "template", None),
                self.create_text(self.lowest_grade, "dynamic", "final_grade"),
                self.create_text(" or above. ", "template", None),
            ]
        else:
            lowest_text = [
                self.create_text("Throughout ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" enrollment in this major, ", "template", None),
                self.create_text(self.pronoun.lower(), "dynamic", "gender"),
                self.create_text(" maintained all ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" grades at ", "template", None),
                self.create_text(self.lowest_grade, "dynamic", "final_grade"),
                self.create_text(". ", "template", None),
            ]
        return lowest_text

    def get_failed_then_passed_text(self):
        failed_then_passed_text = [self.create_text("", "template", None)]
        if self.failed_course != '':
            failed_then_passed = [
                self.create_text(self.pronoun, "dynamic", "gender"),
                self.create_text(" failed the course ", "template", None),
                self.create_text(self.failed_course, "dynamic", "final_grade"),
                self.create_text(" on ", "template", None),
                self.create_text(self.semester_failed_course, "dynamic", "academic_period_desc"),
                self.create_text(", but achieved ", "template", None),
                self.create_text(self.new_grade_f, "dynamic", "final_grade"),
                self.create_text(" retaking the same course in ", "template", None),
                self.create_text(self.semester_passed_course_f, "dynamic", "academic_period_desc"),
                self.create_text(". ", "template", None),
            ]
        return failed_then_passed_text

    def get_grad_text(self):
        grad_text = [self.create_text("", "template", None)]
        if self.grad_ind == False and self.expected_grad_date != "" and self.last_semester_enrolled != "":
            grad_text = [
                self.create_text(self.pronoun, "dynamic", "gender"),
                self.create_text(" did not graduate yet and ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" last semester enrolled was ", "template", None),
                self.create_text(self.last_semester_enrolled, "dynamic", "last_semester_enrolled"),
                self.create_text(", while ", "template", None),
                self.create_text(self.pronoun, "dynamic", "gender"),
                self.create_text(" was expected to graduate in ", "template", None),
                self.create_text(self.expected_grad_date, "dynamic", "expected_grad_date"),
                self.create_text(". ", "template", None),
            ]
            if self.choices[8] == '1' and str(self.recent_gpa) != 'nan' and self.recent_gpa != 0:
                grad_text += [
                    self.create_text(self.pronoun_2.title(), "dynamic", "gender"),
                    self.create_text(" latest GPA is ", "template", None),
                    self.create_text(str(self.recent_gpa), "dynamic", "CGPA"),
                    self.create_text(". ", "template", None),
                ]
        elif self.grad_ind == False and self.expected_grad_date == "" and self.last_semester_enrolled == "":
            grad_text = [
                self.create_text(self.pronoun, "dynamic", "gender"),
                self.create_text(" did not graduate yet and there is no information about ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" expected graduation date. ", "template", None),
            ]
            if self.choices[8] == '1' and str(self.recent_gpa) != 'nan' and self.recent_gpa != 0:
                grad_text += [
                    self.create_text(self.pronoun_2.title(), "dynamic", "gender"),
                    self.create_text(" latest GPA is ", "template", None),
                    self.create_text(str(self.recent_gpa), "dynamic", "CGPA"),
                    self.create_text(". ", "template", None),
                ]
        elif self.grad_ind == False and self.expected_grad_date == "" and self.last_semester_enrolled != "":
            grad_text = [
                self.create_text(self.pronoun, "dynamic", "gender"),
                self.create_text(" did not graduate yet and ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" last semester enrolled was ", "template", None),
                self.create_text(self.last_semester_enrolled, "dynamic", "last_semester_enrolled"),
                self.create_text(". ", "template", None),
            ]
            if self.choices[8] == '1' and str(self.recent_gpa) != 'nan' and self.recent_gpa != 0:
                grad_text += [
                    self.create_text(self.pronoun_2.title(), "dynamic", "gender"),
                    self.create_text(" latest GPA is ", "template", None),
                    self.create_text(str(self.recent_gpa), "dynamic", "CGPA"),
                    self.create_text(". ", "template", None),
                ]
        elif self.grad_ind == False and self.expected_grad_date != "" and self.last_semester_enrolled == "":
            grad_text = [
                self.create_text(self.pronoun, "dynamic", "gender"),
                self.create_text(" did not graduate yet and there is no information about ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" last semester enrolled. ", "template", None),
            ]
            if self.choices[8] == '1' and str(self.recent_gpa) != 'nan' and self.recent_gpa != 0:
                grad_text += [
                    self.create_text(self.pronoun_2.title(), "dynamic", "gender"),
                    self.create_text(" latest GPA is ", "template", None),
                    self.create_text(str(self.recent_gpa), "dynamic", "CGPA"),
                    self.create_text(". ", "template", None),
                ]
        elif self.grad_ind == True:
            grad_text = [
                self.create_text(self.pronoun, "dynamic", "gender"),
                self.create_text(" graduated after ", "template", None),
                self.create_text(self.p.number_to_words(self.semester_count), "dynamic", "semester_count"),
                self.create_text(" semesters in ", "template", None),
                self.create_text(self.graduation_date, "dynamic", "graduation_date"),
                self.create_text(" with a GPA of ", "template", None),
                self.create_text(str(self.graduation_gpa), "dynamic", "graduation_gpa"),
                self.create_text(". ", "template", None),
            ]
        else:
            grad_text = [
                self.create_text(" There is no information about ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "semester_count"),
                self.create_text(" graduation status nor graduation date. ", "template", None),
            ]
            if self.choices[8] == '1' and str(self.recent_gpa) != 'nan' and self.recent_gpa != 0:
                grad_text += [
                    self.create_text(self.pronoun_2.title(), "dynamic", "gender"),
                    self.create_text(" latest GPA is ", "template", None),
                    self.create_text(str(self.recent_gpa), "dynamic", "CGPA"),
                    self.create_text(". ", "template", None),
                ]
        return grad_text

    def get_credits_text(self):
        credits_text = [self.create_text("", "template", None)]

        if self.passed_credits_count == 0:
            credits_text = [
                self.create_text("During ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" study, ", "template", None),
                self.create_text(self.pronoun.lower(), "dynamic", "gender"),
                self.create_text(" has attempted a total of ", "template", None),
                self.create_text(self.p.number_to_words(self.attempted_credits), "dynamic", "attempted_credits"),
                self.create_text(" credit hours and has not passed in any credit hours. ", "template", None),
            ]
        elif self.failed_credits_count == 0 and self.withdrawn_credits_count > 0:
            credits_text = [
                self.create_text("During ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" study, ", "template", None),
                self.create_text(self.pronoun.lower(), "dynamic", "gender"),
                self.create_text(" has attempted a total of ", "template", None),
                self.create_text(self.p.number_to_words(self.attempted_credits), "dynamic", "attempted_credits"),
                self.create_text(" credit hours, ", "template", None),
                self.create_text(self.pronoun.lower(), "dynamic", "gender"),
                self.create_text(" has passed in a total of ", "template", None),
                self.create_text(self.p.number_to_words(self.passed_credits_count), "dynamic", "credits_passed"),
                self.create_text(" credit hours and has not failed in any credit hours. ", "template", None),
                self.create_text(self.pronoun.title(), "dynamic", "gender"),
                self.create_text(" has withdrawn a total of ", "template", None),
                self.create_text(self.p.number_to_words(self.withdrawn_credits_count), "dynamic", "withdrawn_credits"),
                self.create_text(" credit hours. ", "template", None),
            ]
        elif self.failed_credits_count > 0 and self.withdrawn_credits_count == 0:
            credits_text = [
                self.create_text("During ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" study, ", "template", None),
                self.create_text(self.pronoun.lower(), "dynamic", "gender"),
                self.create_text(" has attempted a total of ", "template", None),
                self.create_text(self.p.number_to_words(self.attempted_credits), "dynamic", "attempted_credits"),
                self.create_text(" credit hours, ", "template", None),
                self.create_text(self.pronoun, "dynamic", "gender"),
                self.create_text(" passed in a total of ", "template", None),
                self.create_text(self.p.number_to_words(self.passed_credits_count), "dynamic", "credits_passed"),
                self.create_text(" credit hours and failed in total of ", "template", None),
                self.create_text(self.p.number_to_words(self.failed_credits_count), "dynamic", "credits_failed"),
                self.create_text(" credit hours. ", "template", None),
                self.create_text(self.pronoun.title(), "dynamic", "gender"),
                self.create_text(" has not withdrawn any credit hours. ", "template", None),
            ]
        elif self.failed_credits_count == 0 and self.withdrawn_credits_count == 0:
            credits_text = [
                self.create_text("During ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" study, ", "template", None),
                self.create_text(self.pronoun.lower(), "dynamic", "gender"),
                self.create_text(" has attempted a total of ", "template", None),
                self.create_text(self.p.number_to_words(self.attempted_credits), "dynamic", "attempted_credits"),
                self.create_text(" credit hours, ", "template", None),
                self.create_text(self.pronoun.lower(), "dynamic", "gender"),
                self.create_text(" has passed in a total of ", "template", None),
                self.create_text(self.p.number_to_words(self.passed_credits_count), "dynamic", "credits_passed"),
                self.create_text(" credit hours and has not failed nor withdrawn any credit hours. ", "template", None),
            ]
        elif self.passed_credits_count == self.attempted_credits:
            credits_text = [
                self.create_text("During ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" study, ", "template", None),
                self.create_text(self.pronoun.lower(), "dynamic", "gender"),
                self.create_text(" has attempted a total of ", "template", None),
                self.create_text(self.p.number_to_words(self.attempted_credits), "dynamic", "attempted_credits"),
                self.create_text(" credit hours and has passed in all of them. ", "template", None),
            ]
        else:
            credits_text = [
                self.create_text("During ", "template", None),
                self.create_text(self.pronoun_2, "dynamic", "gender"),
                self.create_text(" study, ", "template", None),
                self.create_text(self.pronoun.lower(), "dynamic", "gender"),
                self.create_text(" has attempted a total of ", "template", None),
                self.create_text(self.p.number_to_words(self.attempted_credits), "dynamic", "attempted_credits"),
                self.create_text(" credit hours. ", "template", None),
                self.create_text(self.pronoun, "dynamic", "gender"),
                self.create_text(" has passed in a total of ", "template", None),
                self.create_text(self.p.number_to_words(self.passed_credits_count), "dynamic", "credits_passed"),
                self.create_text(" credit hours. ", "template", None),
            ]
        return credits_text

    def generate_story(self, std_story):
        complete_story = ''
        for k, v in std_story.items():
            complete_story += ''.join(item['text'] for item in v)
        return complete_story
