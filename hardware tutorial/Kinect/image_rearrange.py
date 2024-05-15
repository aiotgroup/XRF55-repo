import os


def run_case(file_dir):
    for files in os.listdir(file_dir):
        bh = files.split('_')[1]
        if bh == '09' or bh == '36' or bh == '07':
            print(file_dir + '\\' + files, ' to ', file_dir + '\\' + files + '_t')
            os.rename(os.path.join(file_dir, files), os.path.join(file_dir, files + '_t'))
    print('rename complete !')
    for files in os.listdir(file_dir):
        bh = files.split('_')[1]
        cs = files.split('_')[-1]
        if bh == '04' or bh == '33' or bh == '08' or bh == '56' or bh == '57' or bh == '58':
            if int(cs) % 2 == 1:
                if bh == '04' or bh == '33' or bh == '08':
                    if int(cs) == 19:
                        print(file_dir + '\\' + files, ' to ', file_dir + '\\' + files[:-2] + str(
                            int(int(cs) / 2) + 1))
                        os.rename(os.path.join(file_dir, files), os.path.join(file_dir, files[:-2]) + str(
                            int(int(cs) / 2) + 1))

                    else:
                        print(file_dir + '\\' + files, ' to ', file_dir + '\\' + files[:-2] + '0' + str(
                            int(int(cs) / 2) + 1))
                        os.rename(os.path.join(file_dir, files), os.path.join(file_dir, files[:-2]) + '0' + str(
                            int(int(cs) / 2) + 1))

                elif bh == '56':
                    print(file_dir + '\\' + files, ' to ', file_dir + '\\' + files[:-5] + '04_' + str(
                        int(int(cs) / 2) + 1 + 10))
                    os.rename(os.path.join(file_dir, files), os.path.join(file_dir, files[:-5]) + '04_' + str(
                        int(int(cs) / 2) + 1 + 10))

                elif bh == '57':
                    print(file_dir + '\\' + files, ' to ', file_dir + '\\' + files[:-5] + '33_' + str(
                        int(int(cs) / 2) + 1 + 10))
                    os.rename(os.path.join(file_dir, files), os.path.join(file_dir, files[:-5]) + '33_' + str(
                        int(int(cs) / 2) + 1 + 10))

                elif bh == '58':
                    print(file_dir + '\\' + files, ' to ', file_dir + '\\' + files[:-5] + '08_' + str(
                        int(int(cs) / 2) + 1 + 10))
                    os.rename(os.path.join(file_dir, files), os.path.join(file_dir, files[:-5]) + '08_' + str(
                        int(int(cs) / 2) + 1 + 10))

            else:
                # continue
                os.removedirs(os.path.join(file_dir, files))
                print('remove ', file_dir + '\\' + files)
        if bh == '06' or bh == '37' or bh == '10':
            if int(cs) % 2 == 1:
                if int(cs) == 19:
                    print(file_dir + '\\' + files, ' to ', file_dir + '\\' + files[:-2] + str(
                        int(int(cs) / 2) + 1))
                    os.rename(os.path.join(file_dir, files), os.path.join(file_dir, files[:-2]) + str(int(int(cs) / 2) + 1))
                else:
                    print(file_dir + '\\' + files, ' to ', file_dir + '\\' + files[:-2] + '0' + str(
                        int(int(cs) / 2) + 1))
                    os.rename(os.path.join(file_dir, files), os.path.join(file_dir, files[:-2]) + '0' + str(int(int(cs) / 2) + 1))
            else:
                if bh == '06':
                    hz = '09'
                elif bh == '37':
                    hz = '36'
                else:
                    hz = '07'
                if int(files.split('.')[0].split('_')[-1]) == 20:
                    print(file_dir + '\\' + files, ' to ', file_dir + '\\' + files[:-5] + hz + '_' + str(
                        int(int(cs) / 2)))
                    os.rename(os.path.join(file_dir, files), os.path.join(file_dir, files[:-5]) + hz + '_' + str(int(int(cs) / 2)))

                else:
                    print(file_dir + '\\' + files, ' to ', file_dir + '\\' + files[:-5] + hz + '_' + '0' + str(
                        int(int(cs) / 2)))
                    os.rename(os.path.join(file_dir, files), os.path.join(file_dir, files[:-5]) + hz + '_' + '0' + str(
                                  int(int(cs) / 2)))

    for files in os.listdir(file_dir):
        bh = files.split('.')[0].split('_')[1]
        cs = files.split('.')[0].split('_')[-1]
        if (bh == '09' or bh == '36' or bh == '07') and cs == 't':
            if int(files.split('.')[0].split('_')[-2]) % 2 == 1:
                if bh == '09':
                    hz = '06'
                elif bh == '36':
                    hz = '37'
                else:
                    hz = '10'
                os.rename(os.path.join(file_dir, files),
                          os.path.join(file_dir, files[:-7]) + hz + '_' + str(
                              int(int(files.split('_')[-2]) / 2) + 11))
                print(file_dir + '\\' + files, ' to ', file_dir + '\\' + files[:-7] + hz + '_' + str(
                    int(int(files.split('_')[-2]) / 2) + 11))
            else:
                os.rename(os.path.join(file_dir, files),
                          os.path.join(file_dir, files[:-4]) + str(
                              int(int(files.split('_')[-2]) / 2) + 10))
                print(file_dir + '\\' + files, ' to ', file_dir + '\\' + files[:-4] + str(
                    int(int(files.split('_')[-2]) / 2) + 10))


run_case('F:\\mkv_output\\color\\XX\\')
