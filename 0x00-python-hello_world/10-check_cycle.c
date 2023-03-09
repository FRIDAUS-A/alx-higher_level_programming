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

	while (list)
	{
		while (tmp)
		{
			if (list->n == (tmp->next)->n)
				return (1);
			tmp = tmp->next;
		}
		tmp = tmp->next;
		list = (*list).next;
	}
	return (0);
}
