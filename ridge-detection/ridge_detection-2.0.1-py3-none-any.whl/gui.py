from tkinter import Tk,Label,Button,Entry,Checkbutton,BooleanVar,StringVar,filedialog,messagebox,Radiobutton
from ridge_detection.gui_helper import click_exit,show_info,gen_id
from ridge_detection.run import run

def create_win():
    # create the window
    window = Tk()
    window.title("Ridge Detection tool v.1.3.2 ")
    window.geometry("750x650")


    # collect the input param and call the run function
    def clicked():
        if path_to_file.get()=="":
            messagebox.showinfo("ERROR","Select an input file ")
        mandatory_parameters= {"mandatory_parameters":{'Sigma': float(sigma.get()), 'Lower_Threshold': float(lower_Threshold.get()), 'Upper_Threshold': float(upper_Threshold.get()), 'Maximum_Line_Length': float(max_line_len.get()),'Minimum_Line_Length': float(min_line_len.get()), 'Darkline': dark_line_state.get(), 'Overlap_resolution': overlap_state.get()}}
        optional_parameters={"optional_parameters":{'Line_width': float(line_width.get()), 'High_contrast': float(high_contrast.get()), 'Low_contrast': float(low_contrast.get())}}
        further_options={"further_options":{'Correct_position': correct_position_state.get(), 'Estimate_width': estimate_width_state.get(), 'doExtendLine': doExtendLine_state.get(), 'Show_junction_points': show_junction_points_state.get(),'Show_IDs': show_IDs_state.get(), 'Display_results': display_results_state.get(), 'Preview': preview_state.get(), 'Make_Binary': make_Binary_state.get(), 'save_on_disk': save_on_disk_state.get()}}
        cmd = {"path_to_file": path_to_file.get()}
        cmd.update(mandatory_parameters)
        cmd.update(optional_parameters)
        cmd.update(further_options)

        run(param=cmd,folder_save_out=txt_askedDir.get())



    # grid for colletting params
    id_row=gen_id()
    lbl = Label(window, text="path_to_file")
    lbl.grid(column=0, row=id_row.current())
    path_to_file = Entry(window, width=40)
    path_to_file.grid(column=1, row=id_row.current())
    def clicked_file():
        path_to_file.delete(0, 'end')
        selected_file = filedialog.askopenfilenames(initialdir='.')
        path_to_file.insert(0, selected_file)
    def reset_file():
        path_to_file.delete(0, 'end')
    btn_clicked_file = Button(window, text="Set file", command=clicked_file)
    btn_clicked_file.grid(column=2, row=id_row.current())
    btn_clicked_reset_file = Button(window, text="reset file", command=reset_file)
    btn_clicked_reset_file.grid(column=3, row=id_row.current())


    row_asked_Dir = id_row.next()
    lbl = Label(window, text="path_to_directory")
    lbl.grid(column=0, row=row_asked_Dir)
    txt_askedDir = Entry(window, width=30)
    txt_askedDir.grid(column=1, row=row_asked_Dir)
    def clicked_dir():
        selected_dir = filedialog.askdirectory(initialdir='.')
        txt_askedDir.insert(0, selected_dir)
    btn_clicked_dir = Button(window, text="Set directory", command=clicked_dir)
    btn_clicked_dir.grid(column=2, row=row_asked_Dir)



    # Mandatory parameters
    lbl = Label(window, text="")
    lbl.grid(column=0, row=id_row.next())
    lbl = Label(window, text="Mandatory parameters:")
    lbl.grid(column=0, row=id_row.next())
    lbl = Label(window, text="Sigma")
    lbl.grid(column=0, row=id_row.next())
    sigma = Entry(window, width=10,textvariable=StringVar(value="3.39"))
    sigma.grid(column=1, row=id_row.current())
    lbl = Label(window, text="Lower Threshold")
    lbl.grid(column=0, row=id_row.next())
    lower_Threshold = Entry(window, width=10,textvariable=StringVar(value="0.34"))
    lower_Threshold.grid(column=1, row=id_row.current())
    lbl = Label(window, text="Upper Threshold")
    lbl.grid(column=0, row=id_row.next())
    upper_Threshold = Entry(window, width=10,textvariable=StringVar(value="1.02"))
    upper_Threshold.grid(column=1, row=id_row.current())
    lbl = Label(window, text="Maximum Line Length")
    lbl.grid(column=0, row=id_row.next())
    max_line_len = Entry(window, width=10,textvariable=StringVar(value="0"))
    max_line_len.grid(column=1, row=id_row.current())
    lbl = Label(window, text="Minimum Line Length")
    lbl.grid(column=0, row=id_row.next())
    min_line_len = Entry(window, width=10,textvariable=StringVar(value="0"))
    min_line_len.grid(column=1, row=id_row.current())

    lbl = Label(window, text="Darkline")
    lbl.grid(column=0, row=id_row.next())
    dark_line_state = StringVar(value="light")
    rad1 = Radiobutton(window, text='DARK', value="dark", variable=dark_line_state)
    rad2 = Radiobutton(window, text='LIGHT', value="light", variable=dark_line_state)
    rad1.grid(column=1, row=id_row.current())
    rad2.grid(column=2, row=id_row.current())

    lbl = Label(window, text="Overlap_resolution")
    lbl.grid(column=0, row=id_row.next())
    overlap_state = StringVar(value="none")
    rad1 = Radiobutton(window, text='SLOPE', value="slope", variable=overlap_state)
    rad2 = Radiobutton(window, text='NONE', value="none", variable=overlap_state)
    rad1.grid(column=1, row=id_row.current())
    rad2.grid(column=2, row=id_row.current())




    # Optional_parameters params
    lbl = Label(window, text="")
    lbl.grid(column=0, row=id_row.next())
    lbl = Label(window, text="\nOptional parameters:")
    lbl.grid(column=0, row=id_row.next())
    lbl = Label(window, text="Line width")
    lbl.grid(column=0, row=id_row.next())
    line_width = Entry(window, width=10,textvariable=StringVar(value="10.0"))
    line_width.grid(column=1, row=id_row.current())
    lbl = Label(window, text="High contrast")
    lbl.grid(column=0, row=id_row.next())
    high_contrast = Entry(window, width=10,textvariable=StringVar(value="0.0"))
    high_contrast.grid(column=1, row=id_row.current())
    lbl = Label(window, text="Low contrast")
    lbl.grid(column=0, row=id_row.next())
    low_contrast = Entry(window, width=10,textvariable=StringVar(value="0.0"))
    low_contrast.grid(column=1, row=id_row.current())


    # Further_parameters
    lbl = Label(window, text="")
    lbl.grid(column=0, row=id_row.next())
    lbl = Label(window, text="\nFurther parameters:")
    lbl.grid(column=0, row=id_row.next())

    correct_position_state = BooleanVar()
    correct_position_state.set(True)
    correct_position = Checkbutton(window, text='Correct position', var=correct_position_state)
    correct_position.grid(column=1, row=id_row.next())

    estimate_width_state = BooleanVar()
    estimate_width = Checkbutton(window, text='Estimate width', var=estimate_width_state)
    estimate_width.grid(column=1, row=id_row.next())

    doExtendLine_state = BooleanVar()
    doExtendLine_state.set(True)  # set check state
    doExtendLine = Checkbutton(window, text='Do ExtendLine', var=doExtendLine_state)
    doExtendLine.grid(column=1, row=id_row.next())

    show_junction_points_state = BooleanVar()
    show_junction_points_state.set(True)  # set check state
    show_junction_points = Checkbutton(window, text='Show junction points', var=show_junction_points_state)
    show_junction_points.grid(column=1, row=id_row.next())

    show_IDs_state = BooleanVar()
    show_IDs = Checkbutton(window, text='Show IDs', var=show_IDs_state)
    show_IDs.grid(column=1, row=id_row.next())

    display_results_state = BooleanVar()
    display_results_state.set(True)  # set check state
    display_results = Checkbutton(window, text='Display results', var=display_results_state)
    display_results.grid(column=1, row=id_row.next())

    preview_state = BooleanVar()
    preview_state.set(True)  # set check state
    preview = Checkbutton(window, text='Preview', var=preview_state)
    preview.grid(column=1, row=id_row.next())

    make_Binary_state = BooleanVar()
    make_Binary = Checkbutton(window, text='Make Binary', var=make_Binary_state)
    make_Binary.grid(column=1, row=id_row.next())

    save_on_disk_state = BooleanVar()
    save_on_disk_state.set(True)  # set check state
    save_on_disk = Checkbutton(window, text='Save on disk', var=save_on_disk_state)
    save_on_disk.grid(column=1, row=id_row.next())

    lbl = Label(window, text="")
    lbl.grid(column=0, row=id_row.next())
    lbl = Label(window, text="")
    lbl.grid(column=0, row=id_row.next())

    btn = Button(window, text="send parameter",command=clicked)
    btn.grid(column=0, row=id_row.next())


    btn_info = Button(window, text="Info parameters", command=show_info)
    btn_info.grid(column=2, row=id_row.current())

    lbl = Label(window, text="")
    lbl.grid(column=0, row=id_row.next())
    btn2 = Button(window, text="EXIT", command=click_exit)
    btn2.grid(column=2, row=id_row.next())
    window.mainloop()