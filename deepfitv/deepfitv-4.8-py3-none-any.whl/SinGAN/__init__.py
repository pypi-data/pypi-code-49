def help():
    print ("STEPS to use SinGAN")
    a = """1. Copy the code from https://github.com/Virtusa-vLife/DeepFit/tree/master/deepfitv/SinGAN into your local
2. Install the dependencies by running the following command from SinGAN folder location
            python -m pip install -r requirements.txt
3. To train SinGAN model on your own image, put the desire training image under Input/Images, and run

       python main_train.py --input_name <input_file_name>

4. To generate random samples from any starting generation scale, please first train SinGAN model for the desire image (as described above), then run
       python random_samples.py --input_name <training_image_file_name> --mode random_samples --gen_start_scale <generation start scale number>

   For more details please go through the README at https://github.com/Virtusa-vLife/DeepFit/tree/master/deepfitv/SinGAN"""
    print (a)
