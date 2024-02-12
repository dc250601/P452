from . import matrix as mat
import copy
def power_iteration_method(guess,matrix,eps = 1e-6,MAX_ITER = 10000):

    ak_x0 = mat.matmul(matrix,guess)
    ak_x0_y = mat.dot(ak_x0,guess)
    l_old = 0
    i = 0
    while(True):
        i = i+1
        ak_x0_1 = mat.matmul(matrix,ak_x0)
        ak_x0_1_y =mat.dot(ak_x0_1,guess)
        l_new = ak_x0_1_y/ak_x0_y
        ak_x0 = copy.deepcopy(ak_x0_1)
        ak_x0_y = ak_x0_1_y
        if (abs(l_old-l_new)<eps):
            break
        l_old = l_new
        
        if MAX_ITER<i:
            break
        
    mat.normalize_matrix_list(ak_x0)
    return ak_x0,l_new,i
