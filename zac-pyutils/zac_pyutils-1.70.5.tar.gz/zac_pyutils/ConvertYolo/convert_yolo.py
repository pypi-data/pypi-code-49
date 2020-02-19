import sys
import os

def main():
    if sys.argv[1] in ['help','h','-h','--help']:
        print("""
        USAGE: 
          convert_yolo convert <classes_num:int> <darknet_weight_fp>
          convert_yolo detect <classes_names_fp> <tf_weight_fp> <img_fp>
        or:
          python convert_yolo.py convert <classes_num:int> <darknet_weight_fp>
          python convert_yolo.py detect <classes_names_fp> <tf_weight_fp> <img_fp>
        """)
        sys.exit(0)
    print("sys.argv as follow:")
    print(sys.argv)
    try:
        opt=sys.argv[1]
    except Exception as e:
        print("USAGE: python convert_yolo.py {convert,detect}")
        sys.exit(0)
    
    # 不放在开头，因为导入tf耗时很久
    from .utils import load_darknet_weights,draw_outputs
    from ._Yolo_v3 import YoloV3
    import tensorflow as tf
    import numpy as np
    from PIL import Image

    if opt=="convert":
        try:
            classes=int(sys.argv[2])
            darknet_weight_fp=sys.argv[3]
        except:
            print("USAGE: python utils.py convert <classes_num> <darknet_weight_fp>")
            print("Example: python utils.py convert 4 ./custom_w/yolo_w_final.weights")
            sys.exit(0)

        pb_fp=os.path.splitext(darknet_weight_fp)[0]+"_pb"
        print(f"opt:{opt}\nclasses:{classes}\ndarknet_weight_fp:{darknet_weight_fp}\npb_fp:{pb_fp}")

        yolo = YoloV3(classes=classes)

        load_darknet_weights(yolo,darknet_weight_fp)

        # 测试是否正常
        img = np.random.random((1, 320, 320, 3)).astype(np.float32)
        output = yolo(img)
        print("available.")
        
        # yolo.save_weights(os.path.splitext(darknet_weight_fp)[0]+"_ckpt")
        tf.saved_model.save(yolo, pb_fp)
    elif opt=="detect":
        try:
            class_names_fp=sys.argv[2]
            tf_weight_fp=sys.argv[3]
            img_fp=sys.argv[4]
        except:
            print("USAGE: python utils.py detect <classes_names_fp> <tf_weight_fp> <img_fp>")
            sys.exit(0)
        with open(class_names_fp,"r") as fr:
            class_names=[i.strip() for i in fr.readlines()]
            classes=len(class_names)
        print(f"class_names: {','.join(class_names)}")    

        # init yolo
        from _Yolo_v3 import YoloV3
        yolo = YoloV3(classes=classes)
        # load_darknet_weights(yolo,darknet_weight_fp)
        yolo.load_weights(tf_weight_fp)

        # detect img
        img = np.array(Image.open(img_fp).resize((416,416)))
        img = np.expand_dims(img,axis=0)
        boxes, scores, classes, nums = yolo(img)
        img = draw_outputs(img, (boxes[0], scores[0], classes[0], nums[0]), class_names)
        Image.fromarray(img).save("./utils_detected.jpg")
    else:
        print("USAGE: python utils.py {convert,detect}")



if __name__ == "__main__":
    # main()
    print("abc")
