#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: double pointer to head node
 *
 * Return: 0 if not a palindrome, else 1
 */

int is_palindrome(listint_t **head)
{
	int isPalindrome, len, i;
	listint_t *curr, **addresses;

	isPalindrome = 1;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (0);

	/* Get the length of the list */
	for (curr = *head, len = 0; curr != NULL; curr = curr->next)
		len++;

	printf("Len: %d\n", len);

	/* Allocate a array space using the length */
	addresses = malloc(sizeof(listint_t) * len);

	/* Store the addresses in the array */
	for (curr = *head, i = 0; curr != NULL; curr = curr->next, i++)
		addresses[i] = curr;

	for (i = 0; i < len; i++)
	{
		if ((addresses[i])->n != (addresses[len - i - 1])->n)
		{
			isPalindrome = 0;
			break;
		}
	}

	return (isPalindrome);
}
