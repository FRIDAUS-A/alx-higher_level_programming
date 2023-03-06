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
	listint_t *tmp = list;

	if (list == NULL)
		return (0);
	while (list)
	{
		if (list->next == tmp)
			return (1);
		list = (*list).next;
	}
	return (0);
}
