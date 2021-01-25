import os

#메인이 되는 폴더를 지정한다. #생성할 폴더명까지 넣기
main_path = 'C:\\Users\\nugu\\mulra\\envs\\name\\src\\pd\\'

#메인 폴더 생성폴더생성
os.makedirs(main_path[:-1])

#폴더를 생성한다. (폴더 수, 폴더명) - 폴더명0, 폴더명1 이런식으로 증가한다.
def createFolder(x, directory):
    global main_path        
    if x == "0":
        ft_directory = main_path + directory
        try:
            if not os.path.exists(ft_directory):
                os.makedirs(ft_directory)
        except OSError:
            print ('Error: Creating directory. ' +  ft_directory) 
    else:
        for i in range(int(x)):
            ft_directory = main_path + directory + str(i)    
            try:
                if not os.path.exists(ft_directory):
                    os.makedirs(ft_directory)
            except OSError:
                print ('Error: Creating directory. ' +  ft_directory) 

#test 폴더 5개 만들기
createFolder("5", 'test')

#파일을 생성한다. 
mk_dir_lst = os.listdir(main_path) #현재 생성된 폴더를 가져온다.

##현재 생성된 폴더에 파일을 생성한다. 100개씩
for i in mk_dir_lst:    
    for j in range(0, 101):
        with open(main_path + i +"\\" + "frame" + str(j) + ".txt", 'w') as f:
            f.write(" ")

#파일 이름을 바꾼다.
for i in mk_dir_lst:    
    for n, j in enumerate(os.listdir(main_path + i)):                
        os.rename(main_path + i +"\\"+ j, main_path + i +"\\"+ str(i)+str(n)+".txt")

#test1폴더 파일 수 체크
len([os.listdir(main_path+ i) for i in mk_dir_lst][0])

#파일 홀수를 지운다.
for i in mk_dir_lst:
    f_name = main_path + i + "\\"
    for n, j in enumerate(os.listdir(f_name)):        
        if n%2 == True:            
            os.remove(f_name + j)

#test1 폴더 파일 수 체크
len([os.listdir(main_path+ i) for i in mk_dir_lst][0])

#파일들 다 지우기
for i in mk_dir_lst:
    for j in os.listdir(main_path+ i):        
        os.remove(main_path+ i + "\\"+ j)
    print("Delete Complete : " + main_path+ i)

#테스트 폴더 다 지우기
for i in os.listdir(main_path):    
    print("Delete Folder : " + main_path+str(i))
    os.removedirs(main_path+str(i))