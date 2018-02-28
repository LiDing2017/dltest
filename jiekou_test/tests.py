#-*- encoding:utf-8 -*-
# def isPalindrome(s):
#     lens=len(s)
#     l,r=0,lens-1
#     if lens<=1:
#         return False
#     while l<r:
#         if s[l]!=s[r]:
#             return False
#         l+=1
#         r-=1
#         return True
# if __name__ == '__main__':
#     s = 'qabcdefgfedcbaa'
#     print isPalindrome(s)
# import sys
# def binarysearch(array,t):
#     low=0
#     high=len(array)-1
#     mid=(low+high)/2
#     while low<=high:
#         if array[mid]==t:
#             return mid
#         elif array[mid]<t:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1
# print binarysearch(list(range(1,10)),5)
# print [int(i) for i in list(sys.argv[1])]



'''
树的构建：
     5
  6     7
8         9
'''

# class Tree():
#     '树的实现'
#     def __init__(self,ltree=0,rtree=0,data=0):
#         self.ltree = ltree
#         self.rtree = rtree
#         self.data = data
# class BTree():
#     '二叉树的实现'
#     def __init__(self,base = 0):
#         self.base = base
#     def _Empty(self):
#         '是否为空树'
#         if self.base == 0:
#             return True
#         else:
#             return False
#     def qout(self,tree_base):
#         '前序遍历:根-左-右'
#         if tree_base == 0:
#             return
#         print tree_base.data
#         self.qout(tree_base.ltree)
#         self.qout(tree_base.rtree)
#     def mout(self,tree_base):
#         '中序遍历:左-根-右'
#         if tree_base == 0:
#             return
#         self.mout(tree_base.ltree)
#         print tree_base.data
#         self.mout(tree_base.rtree)
#     def hout(self,tree_base):
#         '后序遍历:左-右-根'
#         if tree_base == 0:
#             return
#         self.hout(tree_base.ltree)
#         self.hout(tree_base.rtree)
#         print tree_base.data
# #test
#
# tree1 = Tree(data=8)
# tree2 = Tree(data=9)
# tree3 = Tree(tree1,data=6)
# tree4 = Tree(tree2,0,data=7)
# base = Tree(tree3,tree4,5)
# btree = BTree(base)
# print '前序遍历结果:'
# btree.qout(btree.base)
# print '中序遍历结果:'
# btree.mout(btree.base)
# print '后序遍历结果:'
# btree.hout(btree.base)

# def bulle_sort(lists):
#     count=len(lists)
#     for i in range(count):
#         for j in range(i+1,count):
#             if lists[i]>lists[j]:
#                 lists[i],lists[j]=lists[j],lists[i]
#     return lists
# print bulle_sort([1,9,8,4,7,6,6,3])
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print fact(5)