#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 *
 * @list: linked list node pointer
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{

	listint_t *cur_node;
	int isCycle = 0;

	if (list == NULL || list->next == NULL)
		return (0);

	for (cur_node = list; cur_node != NULL; cur_node = cur_node->next)
	{
		if (cur_node->next == list)
		{
			isCycle = 1;
			break;
		}
		else if (cur_node->next == NULL)
			return (0);
	}

	return (isCycle);
}
