from detectron2.data.datasets import register_coco_instances

# Train set
register_coco_instances(
    "seaclear_train", {},
    "/home/rbu/Comparison_Paper_Object_Detection/Dataset/Seaclear_Marine_Debris_Dataset/annotations/instances_train.json",
    "/home/rbu/Comparison_Paper_Object_Detection/Dataset/Seaclear_Marine_Debris_Dataset/images/train"
)

# Val set
register_coco_instances(
    "seaclear_val", {},
    "/home/rbu/Comparison_Paper_Object_Detection/Dataset/Seaclear_Marine_Debris_Dataset/annotations/instances_val.json",
    "/home/rbu/Comparison_Paper_Object_Detection/Dataset/Seaclear_Marine_Debris_Dataset/images/val"
)

print("✅ SeaClear datasets registered")
