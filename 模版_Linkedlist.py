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
	