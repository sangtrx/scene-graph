
import os.path as osp
import json
from tqdm import tqdm
import os
import shutil
def main():
    path_to_video_list = '/home/tqsang/Sang_SlowFast/list_anet_rescaled_1600.json'
    if osp.isfile(path_to_video_list):
        with open(path_to_video_list, 'r') as f:
            video_list = json.load(f)
    # for video_name in tqdm(video_list[::-1]):
    count = 0
    for video_name in tqdm(video_list):
        folder_name = osp.splitext(osp.basename(video_name))[0]
        output_path = '/media/Seagate16T_sang/scene_graph_output/' + folder_name
        output_predict_path = output_path+'/custom_prediction.json'
        
        if not osp.isfile(output_predict_path):
            shutil.rmtree(output_path)
            continue

        filesize = osp.getsize(output_predict_path)
        if filesize == 0:
            print(output_predict_path)
            os.remove(output_path) 

        # if osp.isfile(output_path):
        #     print(folder_name)
        count += 1
    print(count)


if __name__ == "__main__":
    main()
