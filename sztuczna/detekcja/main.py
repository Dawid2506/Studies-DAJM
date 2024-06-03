# from ultralytics import YOLO
# from roboflow import Roboflow
# import os
#
# rf = Roboflow(api_key="ZArlQIkq4Z4P9CYIsjV1")
# project = rf.workspace("kuchnia").project("kuchnia")
# version = project.version(1)
# dataset = version.download("yolov8")
#
#
# if __name__ == "__main__":
#   data_yaml = os.path.join(dataset.location, "data.yaml")
#
#   model = YOLO('yolov8n.pt')
#
#   model.train(data=data_yaml, epochs=3, imgsz=640, batch=16, name='sings')
#

from ultralytics import YOLO
model = YOLO('C:\\Users\\dawid\\Documents\\GitHub\\Studies DAJM\\runs\\detect\\sings7\\weights\\best.pt')
model.predict(
   source='https://sklep.igadruk.pl/environment/cache/images/0_0_productGfx_1469/kubek-bialy-z-nadrukiem.jpg',
)