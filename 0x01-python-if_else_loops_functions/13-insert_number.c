#include "lists.h"
#include <stdio.h>

/**
 * insert_node - inserts a node in a sorted singly linked list
 *
 * @head: head node double pointer (for modification if necessary)
 * @number: number to insert
 *
 * Return: address of new node, or NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr;
	listint_t *new_node;

	curr = NULL;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}

	for (curr = *head; curr != NULL; curr = curr->next)
	{
		if (number < (*head)->n)
		{
			new_node->next = *head;
			*head = new_node;
			break;
		}
		else if (curr->next == NULL && (number > curr->n))
		{
			curr->next = new_node;
			new_node->next = NULL;
			break;
		}
		else if ((number >= curr->n) && (number <= (curr->next)->n))
		{
			new_node->next = curr->next;
			curr->next = new_node;
			break;
		}
	}

	return (curr);
}
