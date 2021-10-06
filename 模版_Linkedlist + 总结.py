#模版1 创建linkedList 不断添加尾巴 LC 2
head = curr = ListNode(None) 
while loop:
	carry, num = divmod(carry, 10)
	curr.next = ListNode(num)
	curr = curr.next
return header.next



#模版2 创建linkedList 不断添加header LC 445
node = None
while loop:
	carry, num = divmod(carry, 10)
	header = ListNode(num)
	header.next = node
	node = header
return header
	
	

10/04/2021
总结:

1. 递归的写法一般track 的node 比iter 的写法少
2. 单向linkedlist 一般考察的就是移除倒数第几个node, 或者从中间拆开
3. 双向linkedlist 更多考的是设计题, 类似于LFU 之类的