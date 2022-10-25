def rotate(matrix):
    temp_matrix = [*matrix]
    for i in range(len(temp_matrix)):
        matrix[i] = ([row[i] for row in temp_matrix][::-1])
            



def main():
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print(1,matrix)
    rotate(matrix)
    print(2,matrix)
    correct_matrix = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    print(correct_matrix)
    if matrix != correct_matrix:
        print('uh oh')
    else:
        print('hell ya')
    
if __name__ == "__main__":
    main()
