import ctypes

try:
    dll_file_path = "capifwb.so"
    lib = ctypes.cdll.LoadLibrary(dll_file_path)
    print(dll_file_path,"dll is loaded successfully")
except Exception as e:
        print("An exception occurred while loading dll", e)
        print("Failed to load dll at:", dll_file_path)
        quit()

