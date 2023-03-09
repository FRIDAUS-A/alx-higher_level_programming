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
	listint_t *tmp = list, *first = list;

	while (list)
	{
		while (tmp)
		{
			tmp = tmp->next;
			if (list->n == tmp->n)
				return (1);
		}
		list = (*list).next;
		tmp = list;
	}
	return (0);
}
