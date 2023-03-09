#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check for cycle in a linked list
 * @list: stores address of the first node
 * Return: Allow success
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow != NULL && (fast->next) != NULL)
	{
		slow = slow->next;
		fast = (fast->next)->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
