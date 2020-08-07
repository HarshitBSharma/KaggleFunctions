def plot_random_images(image_files_list, image_path, nrows=3, ncols=4, main_title=""):
    """
    image_files_list : List containing all of the image files, stacked on axis 0
    nrows            : Number of rows of pictures
    ncols            : Number of columns of pictures
    main_title       : Main title for sub-plots
    """
    
    # Selecting a random number of images from the given list
    random_img_list = np.random.choice(image_files_list, nrows * ncols)
    
    # Reading images and appending them to the image_matrix_list
    image_matrix_list = []
    for file in random_img_list:
        img = cv2.imread(os.path.join(image_path, file))
        image_matrix_list.append(img)
        
    # Setting the subplots as per inputs provided
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize = (20, 15), squeeze=False)
    fig.suptitle('Wheat', fontsize=30)
    num=0
    for i in range(nrows):
        for j in range(ncols):
            axes[i][j].imshow(image_matrix_list[num])
            axes[i][j].set_title(random_img_list[num], fontsize=14)
            num += 1
    plt.show()



def draw_images_with_bboxes(images_list, image_annotation_file, nrows, ncols, main_title=""):
    image_matrix = []
    random_list = np.random.choice(images_list, 12)
    for image in random_list:
        img = cv2.imread(os.path.join(train_path, image))
        img_df = image_annotation_file.loc[image_annotation_file['image_id'] == image, ["x_min", "y_min", "x_max", "y_max"]]
        bboxes = np.array(img_df.values.tolist())

        for i,bbox in enumerate(bboxes):
            pt1 = (int(bbox[0]), int(bbox[1]))
            pt2 = (int(bbox[2]), int(bbox[3]))
            img = cv2.rectangle(img, pt1, pt2, (255, 0, 0), 5)

        image_matrix.append(img)
    fig, axes = plt.subplots(nrows, ncols, figsize=(20, 15))
    fig.suptitle(main_title, fontsize=30)
    num = 0
    for i in range(nrows):
        for j in range(ncols):
            axes[i][j].imshow(image_matrix[num])
            axes[i][j].set_title(random_list[num], fontsize=14)
            num += 1