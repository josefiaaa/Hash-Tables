

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = (( hash << 5 ) + hash ) + ord( x )
    return hash % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    index = hash( key, hash_table.capacity )
    pair = Pair(key, value)

    if hash_table.storage[index] is not None:
        #if the bucket is not empty 
        if hash_table.storage[index].key != key:
            # checking to see if these keys are different
            # if there is already something stored at this address print a warning:
            f"This address already has information stored! are you sure you want to override {hash_table.storage[index].key}?"
    # if the value des not already exist, add the pair to hash_table:
    hash_table.storage[index] = pair

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    
    if hash_table.storage[index] is None:
        f'Unable to remove item with key: {key}'
    elif hash_table.storage[index].key != key:
        f'Unable to remove item with key: {key}'
    else:
        hash_table.storage[index] = None

# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    # STEP 1
    index = hash(key, hash_table.capacity)
    # STEP 2
    # if there's nothing in that bucket at all:
    if hash_table.storage[index] is None:
        return None
    #STEP 3
    #if the key is not found
    # look in the storage of our hashed table at that particular index and the keys don't match:
    elif hash_table.storage[index] is not None and hash_table.storage[index].key != key:
        return None
    #key is found
    else:
        #STEP 4
        #return the VALUE
        return hash_table.storage[index].value

# recap:
#   STEP 1: we are getting the index of where this value would exist in our hashtable if it's there at all
#   STEP 2: Check if there's anything in that bucket in the first place
#   STEP 3: check if theres something in our hashtable then check to see if there's something with this particular key, if not, return None 
#   STEP 4: return the value at that index location



def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
