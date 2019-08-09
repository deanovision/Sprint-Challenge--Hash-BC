#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        key = weights[i]
        value = i
        print("key", key, "value", value)
        hash_table_insert(ht, key, value)
    for i in range(ht.capacity):
        if ht.storage[i] != None:
            target = limit - ht.storage[i].key
            current = ht.storage[i].value
            if hash_table_retrieve(ht, target) is not None:
                print("target", target, "key", ht.storage[i].key, "current", current,
                      "target_index", hash_table_retrieve(ht, target))
                target_index = hash_table_retrieve(ht, target)
                if current > target_index:
                    answer = (ht.storage[i].value,
                              hash_table_retrieve(ht, target))
                    print(answer)
                    return answer
                else:
                    if hash_table_retrieve(ht, target) == 1:
                        answer = (hash_table_retrieve(ht, target), 0)
                        print(answer)
                        return answer
                    else:
                        answer = (hash_table_retrieve(
                            ht, target), ht.storage[i].value)
                        print(answer)
                        return answer
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
