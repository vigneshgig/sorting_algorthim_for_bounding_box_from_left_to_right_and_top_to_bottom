import numpy as np 
import scipy.spatial.distance as distance
 
def sorting_bounding_box(points):
    
    points = list(map(lambda x:[x[0],x[1][0],x[1][2]],points))
    # print(points)
    points_sum = list(map(lambda x: [x[0],x[1],sum(x[1]),x[2][1]],points))
    x_y_cordinate = list(map(lambda x: x[1],points_sum))
    final_sorted_list = []
    while True:
        try:
            new_sorted_text = []
            initial_value_A  = [i for i in sorted(enumerate(points_sum), key=lambda x:x[1][2])][0]
    #         print(initial_value_A)
            threshold_value = abs(initial_value_A[1][1][1] - initial_value_A[1][3])
            threshold_value = (threshold_value/2) + 5
            del points_sum[initial_value_A[0]]
            del x_y_cordinate[initial_value_A[0]]
    #         print(threshold_value)
            A = [initial_value_A[1][1]]
            K = list(map(lambda x:[x,abs(x[1]-initial_value_A[1][1][1])],x_y_cordinate))
            K = [[count,i]for count,i in enumerate(K)]
            K = [i for i in K if i[1][1] <= threshold_value]
            sorted_K = list(map(lambda x:[x[0],x[1][0]],sorted(K,key=lambda x:x[1][1])))
            B = []
            points_index = []
            for tmp_K in sorted_K:
                points_index.append(tmp_K[0])
                B.append(tmp_K[1])
            dist = distance.cdist(A,B)[0]
            d_index = [i for i in sorted(zip(dist,points_index), key=lambda x:x[0])]
            new_sorted_text.append(initial_value_A[1][0])

            index = []
            for j in d_index:
                new_sorted_text.append(points_sum[j[1]][0])
                index.append(j[1])
            for n in sorted(index, reverse=True):
                del points_sum[n]
                del x_y_cordinate[n]
            final_sorted_list.append(new_sorted_text)
            # print(new_sorted_text)
        except Exception as e:
            print(e)
            break

    return final_sorted_list
if  __name__ == '__main__':
# example points
    points = [['11/10,', [[466.66666, 261.33334],
       [532.     , 261.33334],
       [532.     , 285.33334],
       [466.66666, 285.33334]]],
       ['st', [[556.     , 261.33334],
       [582.6667 , 261.33334],
       [582.6667 , 285.33334],
       [556.     , 285.33334]]], ['Str', [[586.6667 , 261.33334],
       [626.6667 , 261.33334],
       [626.6667 , 285.33334],
       [586.6667 , 285.33334]]], ['R', [[377.33334, 262.66666],
       [400.     , 262.66666],
       [400.     , 285.33334],
       [377.33334, 285.33334]]], ['si.', [[410.66666, 264.     ],
       [442.66666, 264.     ],
       [442.66666, 285.33334],
       [410.66666, 285.33334]]], ['1.', [[544.     , 264.     ],
       [561.3333 , 264.     ],
       [561.3333 , 285.33334],
       [544.     , 285.33334]]], ['et,', [[637.3333, 264.    ],
       [670.6667, 264.    ],
       [670.6667, 288.    ],
       [637.3333, 288.    ]]], ['et', [[396.     , 265.33334],
       [414.66666, 265.33334],
       [414.66666, 285.33334],
       [396.     , 285.33334]]], ["'el", [[622.6667 , 265.33334],
       [641.3333 , 265.33334],
       [641.3333 , 285.33334],
       [622.6667 , 285.33334]]], ['in', [[529.3333 , 276.     ],
       [537.3333 , 276.     ],
       [537.3333 , 285.33334],
       [529.3333 , 285.33334]]], ['Corporati', [[378.73196, 287.75485],
       [482.9534 , 289.35825],
       [482.57034, 314.25494],
       [378.3489 , 312.65155]]], ['ion', [[478.66666, 288.     ],
       [518.6667 , 288.     ],
       [518.6667 , 309.33334],
       [478.66666, 309.33334]]], ['Colony,', [[525.82104, 285.5305 ],
       [614.4748 , 291.07132],
       [613.00653, 314.5629 ],
       [524.3528 , 309.02206]]], ['T.Nafgg,', [[377.85098, 309.27054],
       [470.8392 , 316.4235 ],
       [468.88623, 341.81174],
       [375.89804, 334.65878]]], ['Chennai', [[476.     , 313.33334],
       [566.6667 , 313.33334],
       [566.6667 , 336.     ],
       [476.     , 336.     ]]], ['48.', [[592.     , 313.33334],
       [626.6667 , 313.33334],
       [626.6667 , 334.66666],
       [592.     , 334.66666]]]]
    print(sorting_bounding_box(points))
    

