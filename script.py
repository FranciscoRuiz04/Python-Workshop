###############################################################################
################################   Baby steps  ################################




# First of all, we need to read the file.
# To reduce number of code lines save the pathfile into a variable,
# since we going to use it at several times.
filepath = 'SMN_1151.html'

# # WHAT DOES open() FUNCTION DO????
# # open() is a built-in function. It will read our file completely.
# # But to have major control over the file content, one option is to iterate
# # over every text line.
# file = open(filepath, encoding='utf-8')
# for line in file:
#     print(line)
# # ¡¡¡¡ Never forget to close your file !!!! #
# file.close()




# # To avoid running unneccesary code lines and to improve the code handling
# # use functions.

# # ++++ sorter() function 1.0 version ++++ #
# def sorter(filepath):
#     # Read file and get every text line
#     # try:
#     file = open(filepath, encoding='utf-8')
#     for line in file:
#         print(line)
#     file.close()
#     # except:
#     #     print('There has occured an error!')


# # # ¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡ #
# # # ¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡   Code Testing   !!!!!!!!!!!!!!!!!!!!!!! #
# # # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #










# # ++++ sorter() function 1.1 version ++++ #
# def sorter(filepath, ignore_nlines=1):
#     # Read file and get every text line
#     try:
#         file = open(filepath, encoding='utf-8')
#         for n,line in enumerate(file):
#             # Ignore n (ignore_nlines) number of text lines
#             if n >= ignore_nlines: 
#                 print(line)
#         file.close()
#     except:
#         print('There has occured an error!')
# # WHAT DOES enumerate() FUNCTION DO????
# # enumerate() is a built-in function. With it we'll get a tuple data type
# # with two values within; the number of item and the item itself.


# # # ¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡ #
# # # ¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡   Code Testing   !!!!!!!!!!!!!!!!!!!!!!! #
# # # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #










# # ++++ sorter() function 1.2 version ++++ #
# def sorter(filepath, ignore_nlines=1, colnames=False):
#     # Read file and get every text line
#     lines = []
#     try:
#         file = open(filepath, encoding='utf-8')
#         for n,line in enumerate(file):
#             # Ignore n (ignore_nlines) number of text lines
#             if n >= ignore_nlines: 
#                 lines.append(line.split())
#         file.close()
    
#     except:
#         print('There has occured an error!')
    
#     else:
#         # Create a container to separate by data elements (text and amounts)
#         content = {}
#         # Only data of interest
#         data = []
        
#         # Processing to get the data which will fill our rows
#         # Since we know that the first line (the first list item) has the column names
#         # we need to fetch and save it
#         for i, record in enumerate(lines):
#             # Data filtering by number of items. Consider solely those which may have
#             # relevant information
#             if len(record) > 4:
#                 if i == 0 and colnames:
#                     # Save column names into our "content" dictionary with "COLNAMES" as key
#                     content["COLNAMES"] = record
#                 # For the rest of the data save it into a particular list type element
#                 else:
#                     data.append(record)
        
#         # Assign to our "content" dictionary the key named as "DATA" where will be saved 
#         # the data of interest
#         content['DATA'] = data
#         return content  # What does "return" reserved word do???? Returns an usable object
#         # What's the difference between "return" and "print"????


# # # ¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡ #
# # # ¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡   Code Testing   !!!!!!!!!!!!!!!!!!!!!!! #
# # # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #










# ###########################     1st Part Ending     ###########################
# ###############################################################################




















# ###############################################################################
# ###########################     The Final Function  ###########################


# # ---- recordFormatter() function 1.0 version ---- #
# def recordFormatter(tline):
#     # Each text line consists of alphabetic and numeric data types
#     # The alphabetic part consists of spaces between words; "Fecha Maxima Diaria", for instance.
#     # This could cause an error at the fill in moment
#     wordsOnly = []
#     filteredRecords = []
    
#     # We need to evaluate each item from the text line
#     for item in tline:
#         # Sort items. Either Alphabetic or Numeric data type 
#         if item.isalpha():  # What does isalpha() built-in function do???? Assert
#             wordsOnly.append(item)
#         else:
#             filteredRecords.append(item)
    
#     wordsOnly = '_'.join(wordsOnly)
#     # Create your last record structure. 
#     filteredRecords.insert(0, wordsOnly)
#     # What's the difference between insert() and append() functions???? Handling
    
#     return tuple(filteredRecords)


# # # ¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡ #
# # # ¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡   Code Testing   !!!!!!!!!!!!!!!!!!!!!!! #
# # # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# # testRecord = ['FECHA', 'MINIMA', 'DIARIA', '14/1986', '24/1976', '02/1974', '01/1987', '11/1966', '16/1979', '18/1989', '27/1970', '27/1979', '23/1989', '17/1970', '14/1997']










# # \\\\   sorter(), the final function    \\\\ #
# def sorter(filepath, ignore_nlines=1, colnames=False):
#     # Read file and get every text line
#     lines = []
#     try:
#         file = open(filepath, encoding='utf-8')
#         for n,line in enumerate(file):
#             # Ignore n (ignore_nlines) number of text lines
#             if n >= ignore_nlines: 
#                 lines.append(line.split())
#         file.close()
    
#     except:
#         print('There has occured an error!')
    
#     else:
#         # Create a container to separate by data elements (text and amounts)
#         content = {}
#         # Only data of interest
#         data = []
    
#         # Processing to get the data which will fill our rows
#     for i, record in enumerate(lines):
#         # Data filtering by number of items.
#         if len(record) > 4:
#                 if i == 0 and colnames:
#                     # Save column names into our "content" dictionary with "COLNAMES" as key
#                     content["COLNAMES"] = record
#                 # For the rest of the data save it into a particular list type element
#                 else:
#                     # Give a correct record format
#                     formattedRecord = recordFormatter(record)
#                     # Get a list with every record in it
#                     data.append(formattedRecord)
#     content["DATA"] = data
    
#     return content


# # ¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡ #
# # ¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡   Code Testing   !!!!!!!!!!!!!!!!!!!!!!! #
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #










# ####################################################################
# ####################    Playing with the Panda  ####################

# # Import the package
# import pandas as pd

# # Run your sorter() function and save the outcome into a variable to use it later
# mydata = sorter(filepath=filepath, ignore_nlines=4, colnames=True)

# # Create your first DataFrame
# df = pd.DataFrame(mydata["DATA"], columns=mydata["COLNAMES"])


# # Export the DataFrame to csv file
# outPath = './TYPE_YOUR_NAME.csv'
# df.to_csv(outPath, encoding='utf-8', index=False)