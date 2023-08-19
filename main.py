import pandas as pd
import time

search_excel = pd.read_excel('Search.xlsx')
tag_list = pd.read_excel('Taglist.xlsx')

tag_list['TagShort'] = 'Not Found'

start_time = time.time()
for index, row in tag_list.iterrows():
    cell_value = row['Tag']
    input_word = cell_value.split()

    tag_short_list = []
    for word in input_word:
        found_row = search_excel[search_excel['Tag'] == word]
        if not found_row.empty:
            tag_short_list.append(found_row.iloc[0]['Short'])
        else:
            tag_short_list.append(word)

    tag = '_'.join(tag_short_list)
    tag_list.at[index, 'TagShort'] = tag

end_time = time.time()
print(end_time-start_time)
tag_list.to_excel('Updated.xlsx', index=False)
