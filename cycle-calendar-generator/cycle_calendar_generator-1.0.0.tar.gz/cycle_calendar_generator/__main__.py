from .cycle_calendar_generator import (
        getArgs,
        readScheduleSetupFile,
        parseScheduleSetup,
        userScheduleFileScanner,
        ALL_DONE)


def main():
    folder = getArgs()
    setup_file = readScheduleSetupFile(folder)
    setup_data = parseScheduleSetup(setup_file)
    if userScheduleFileScanner(setup_data, folder):
        print(ALL_DONE)


if __name__ == "__main__":
    main()
