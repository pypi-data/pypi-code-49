"""
smarty
~~~~~~

This is a instance management CLI for SmartRecruiters solutions consulting.
"""

import json
import os
import sys
import time

from smarty_py import utils
from smarty_py.api import CandidateAPI

from colorama import init

init()
from colorama import Fore, Back, Style

clear = lambda: os.system("cls" if os.name == "nt" else "clear")

BASE_URL = "https://api.smartrecruiters.com"


def main():
    clear()

    print(Fore.GREEN + "Welcome to Smarty Py v2.0" + Fore.RESET)

    token = input(
        "If you have a token saved, press enter to choose. "
        "Otherwise, please enter your SmartToken to begin:\n"
    )
    if token:
        try:
            instance = utils.get_instance(token)
        except:  # handle auth error
            print(
                Fore.RED
                + "Error 01 - Invalid SmartToken; please try again."
                + Fore.RESET
            )

            time.sleep(1)

            main()
        else:  # store new token
            instance["token"] = token
            utils.save_token(instance["token"], instance["name"])

            menu(instance)
    else:
        tokens = utils.get_tokens()
        print(Fore.CYAN + "Select a token from the following:" + Fore.RESET)
        for i, pair in enumerate(tokens):
            print(Fore.LIGHTYELLOW_EX + f"{i + 1}. {pair[0]} | {pair[1]}" + Fore.RESET)

        selection = input("\nSelection: ")

        try:
            print("\nLoading instance...")
            instance = utils.get_instance(tokens[int(selection) - 1][1])
        except:  # handle auth error
            print(
                Fore.RED
                + "Error 01 - Invalid SmartToken; please try again."
                + Fore.RESET
            )
            time.sleep(2)

            main()
        else:
            instance["token"] = tokens[int(selection) - 1][1]

            menu(instance)


def menu(instance):
    """ CLI: Main Menu

    Direct user to other CLI methods.

    :param instance: a `dict` of instance information.
    """
    clear()

    print(
        Fore.GREEN
        + f"Current Instance: {instance['name']} {instance['type']}"
        + Fore.RESET
    )
    print(Fore.CYAN + "Main Menu - Select an Action" + Fore.RESET)
    print(
        Fore.LIGHTYELLOW_EX
        + """
        1. Manage Candidates
        2. Exit
        """
        + Fore.RESET
    )

    selection = input("Selection: ")
    if selection == "1":
        manage_candidates(instance)
    elif selection == "2":
        clear()

        print(Fore.GREEN + "Thanks for using Smarty Py!" + Fore.RESET)

        sys.exit()
    else:
        print("Invalid input. Please try again.")

        time.sleep(1)

        menu(instance)


def manage_candidates(instance):
    """ CLI: Candidates Menu

    List options regarding candidate management,
    each tied to one or more smartlib functions.

    Arguments:
        instance -- a dictionary of SR instance information
    
    """
    print("Loading CandidateAPI client...")
    api = CandidateAPI(instance["token"])

    clear()

    print(Fore.GREEN + "Current Instance: %s" % (instance["name"]) + Fore.RESET)
    print(Fore.CYAN + "Candidates Menu - Select an Action" + Fore.RESET)
    print(
        Fore.LIGHTYELLOW_EX
        + """
        1. Search Candidates
        2. Add Candidate
        3. Add Candidate and Assign to Job
        4. Get Candidate Info
        5. Return to Main Menu
        """
        + Fore.RESET
    )

    selection = input("Selection: ")
    if selection == "1":  # search candidates
        clear()

        print(Fore.GREEN + "Current Instance: %s" % (instance["name"]) + Fore.RESET)
        print(Fore.CYAN + "Candidate Search\n" + Fore.RESET)

        q = input("Search Term: ")
        l = input("Limit: ")
        o = input("Offset: ")
        try:
            print("\nSearching candidates...")
            results = api.search(params={"q": q, "limit": l, "offset": o})
        except:
            print(
                Fore.RED
                + "\nThere are no candidates matching that search term."
                + Fore.RESET
            )
        else:
            if results:
                print(
                    Fore.CYAN
                    + f"\n{results['totalFound']} Total | Search Results:\n"
                    + Fore.RESET
                )

                for r in results["content"]:
                    print(
                        Fore.MAGENTA
                        + f"{r['firstName']} {r['lastName']} | {r['id']}"
                        + Fore.RESET
                    )
            else:
                print(
                    Fore.RED
                    + "\nThere are no candidates matching that search term."
                    + Fore.RESET
                )

        action = input("\nPress enter to return to Candidate Management.")
        if action == "":
            manage_candidates(instance)

    elif selection == "2":  # add candidates
        clear()

        print(Fore.GREEN + "Current Instance: %s" % (instance["name"]) + Fore.RESET)
        print(Fore.CYAN + "Candidate Creation\n" + Fore.RESET)

        number = input("Number of candidates to add: ")
        for _ in range(int(number)):
            candidate = utils.create_candidate(instance)

            try:
                print("\nAdding candidates...")
                response = api.create(**candidate)
            except:
                print(
                    Fore.RED + "There was an error adding that candidate." + Fore.RESET
                )
            else:
                print(
                    Fore.YELLOW
                    + f"Candidate added: {response['firstName']} {response['lastName']}"
                    + Fore.RESET
                )

        action = input("\nPress enter to return to Candidate Management.")
        if action == "":
            manage_candidates(instance)

    elif selection == "3":  # add and assign candidate to job
        clear()

        print(Fore.GREEN + "Current Instance: %s" % (instance["name"]) + Fore.RESET)
        print(Fore.CYAN + "Candidate Creation and Assignment\n" + Fore.RESET)

        job_id = input("Job ID: ")
        number = input("Number of candidates to add and assign: ")
        for _ in range(int(number)):
            candidate = utils.create_candidate(instance)

            try:
                print("\nAdding candidates...")
                response = api.create_and_assign(job_id, **candidate)
            except:
                print(
                    Fore.RED
                    + "There was an error adding and assigning that candidate."
                    + Fore.RESET
                )
            else:
                print(
                    Fore.YELLOW
                    + f"Candidate added: {response['firstName']} {response['lastName']}"
                    + Fore.RESET
                )

        action = input("\nPress enter to return to Candidate Management.")
        if action == "":
            manage_candidates(instance)

    elif selection == "4":  # get candidate details
        clear()

        print(Fore.GREEN + "Current Instance: %s" % (instance["name"]) + Fore.RESET)
        print(Fore.CYAN + "Candidate Info\n" + Fore.RESET)

        candidate_id = input("Candidate ID: ")

        try:
            print("\nRetrieving candidate data...")
            response = api.get(candidate_id)
        except ValueError:
            print(Fore.RED + "\nInvalid input; try again." + Fore.RESET)
        except:
            print(Fore.RED + "\nThat ID does not match a candidate." + Fore.RESET)
        else:
            print(
                Fore.YELLOW
                + f"""
            {response['firstName']} {response['lastName']}
            {response['email']}
            https://www.smartrecruiters.com/app/people/candidates/{response['id']}
            """
                + Fore.RESET
            )

        action = input("\nPress enter to return to Candidate Management.")
        if action == "":
            manage_candidates(instance)

    elif selection == "5":
        menu(instance)

    else:
        print("Invalid input. Please try again.")

        time.sleep(1)

        manage_candidates(instance)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()

        print(Fore.GREEN + "Thanks for using smarty.py!" + Fore.RESET)
