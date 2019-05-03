class Sol:
    def intersection_of_arr_II(self,arr1,arr2):
        list=[]
        for num in arr1:
            if num in arr2:
                list.append(num)
                arr2.remove(num)
        return list


if __name__ == '__main__':
    p1=Sol()
    print(p1.intersection_of_arr_II([2,4,8,4,4],[7,4,4,8,3]))
