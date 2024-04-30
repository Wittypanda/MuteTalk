import cv2, os

#Simply performing ETL process 
#Why ETL ? Well to increase the combinations & possible orientation using rotation scaling etc thus Extracting Transforming & Then loading the images 

def flip_images():
	gest_folder = "gestures"
	images_labels = []
	images = []
	labels = []
	for g_id in os.listdir(gest_folder):
		for i in range(1200):
			path = gest_folder+"/"+g_id+"/"+str(i+1)+".jpg"
			new_path = gest_folder+"/"+g_id+"/"+str(i+1+1200)+".jpg"
			print(path)
			img = cv2.imread(path, 0)
			img = cv2.flip(img, 1)
			cv2.imwrite(new_path, img)

flip_images()
