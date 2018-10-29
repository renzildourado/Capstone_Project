import pandas as pd


def open_file():
    file_name = "dataset.csv"
    data_frame = pd.read_csv(file_name, low_memory=False)
    return data_frame


def one_hot_encoding(data_frame):
    data_frame= pd.concat([data_frame, pd.get_dummies(data_frame['CATEGORY'], prefix='CATEGORY')], axis=1).drop(['CATEGORY'], axis=1)
    data_frame.to_csv("cleaned_dataset_3.csv", index=False)


def encode_target_attribute(data_frame):
    data_frame.loc[data_frame["MALWARE_DETECTION"]>=1,"MALWARE_DETECTION"] = 1
    data_frame.to_csv("cleaned_dataset_2.csv", index=False)


def get_rid_of_unwanted_attributes(data_frame):
    columns_to_delete = {}
    for column in data_frame:
        if column == "CATEGORY" or column =="APK_NAME" or column == " MALWARE_DETECTION_COUNT":
            continue
        count = 0
        total = len(data_frame[column])
        for element in data_frame[column]:
            if element == 1:
                count += 1
        if count/total <=0.1:
            columns_to_delete[column] = count

    print(len(columns_to_delete))
    list_of_columns_to_delete = list(columns_to_delete.keys())

    cleaned_data_frame = data_frame.drop(columns = list_of_columns_to_delete)
    cleaned_data_frame.to_csv("cleaned_dataset_1.csv", index=False)


def main():
    data_frame = open_file()
    get_rid_of_unwanted_attributes(data_frame)
    # encode_target_attribute(data_frame)
    # one_hot_encoding(data_frame)


if __name__ =='__main__':
    main()