# from Salicon import Salicon
import matplotlib.pyplot as plt
import numpy as np
import os
import imageio

class test_salicon():
    """
    use the pretrained model to get the saliency map
    """

    def __init__(self):
        # self.sal = Salicon()
        pass

    def get_saliency_one_image(self, image_path):
        """
        get the saliency map in a grey image
        """
        map = self.sal.compute_saliency(image_path)
        'for debug'
        # print('>>>>>>>>>>>>>>>>>>..map', map, np.shape(map))
        plt.imshow(map)
        plt.show()

        return map


    def run_cube_6_in_6(self):
        """
        get jianyi's cube_6_in_6
        """
        import os

        image_path = '/home/ml/OpenSALICON/cube_6_in_6/'
        all_file =  os.listdir(image_path)

        for i_step in range(len(all_file)):
            for i_image in range(6):
                image_path = all_file[ i_step ] + '/' + 'BlueWorld_%03d'%i_image + '.jpg'
                # img = imageio.imread(image_path)
                print('>>>>>>>>>>>>>>>>: ', image_path)



        print(">>>>>>>>>>>>>: ", all_file)


    def save_heatmap(self,heatmap,path,name):
        """
        save hmap
        """
        if os.path.exists(path) is False:
            os.mkdir(path)
        heatmap = heatmap * 255.0
        imageio.imwrite(path+ '_'+name+'.png',heatmap)

    def run(self):

        image_path = 'face.jpg'
        save_path = 'result/'
        name = 'test_face_saliency_output'

        hmap = self.get_saliency_one_image(image_path)
        self.save_heatmap(heatmap=hmap,
                          path=save_path,
                          name=name)

if __name__ == '__main__':
    sal = test_salicon()
    sal.run_cube_6_in_6()
