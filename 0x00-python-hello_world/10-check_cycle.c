#include "lists.h"

/**
 * listint_t - Checks if a singly linked list has a cycle in it
 *
 * list: linked list node pointer
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	int isCycle = 0, tot_itr_count = 0;
	listint_t *cur_node, *head = list;

	for (cur_node = list; cur_node != NULL; cur_node++)
	{
		tot_itr_count++;

		if (cur_node == NULL)
		{
			isCycle = 0;
			break;
		}
		else if (tot_itr_count > 0 && cur_node == head)
		{
			isCycle = 1;
			break;
		}
	}

	return (isCycle);
}
