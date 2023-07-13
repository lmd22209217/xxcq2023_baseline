import json

with open("train_1.json", 'r', encoding='utf-8') as f:
    data1 = f.readlines()

with open("test_1.txt", 'r', encoding='utf-8') as f:
    data2 = f.readlines()

new_data1 = []
for d in data1:
    old_data = json.loads(d)
    # print(old_data)
    relationMentions = []
    for dr in old_data["relationMentions"]:
        triple = [dr['em1Text'], dr['label'], dr['em2Text']]
        relationMentions.append(triple)
    new_data1.append({
        "text": old_data['sentText'],
        "spo_list": relationMentions
    })

new_data2 = []
for d in data2:
    # print(d)
    new_data2.append({
        "text": d.replace("\"","").replace("\n",""),
        "spo_list": []
    })

json.dump(new_data1, open('train_triples.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
json.dump(new_data2, open('test_triples.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)

