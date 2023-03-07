#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a number into a sorted link
 * @head: stores the address of the pointer to the variable
 * @number: number to be inserted
 * Return: Allow success
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *before, *tmp, *first;

	first = *head;
	new = (listint_t *)malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	while (*head)
	{
		if ((*head)->n > number)
		{
			tmp = *head;
			break;
		}
		before = *head;
		*head = (*head)->next;
	}
	if (*head)
	{
		before->next = new;
		new->next = tmp;
	}
	else
	{
		(*head)->next = new;
		new->next = NULL;
	}
	*head = first;
	return (new);
}
