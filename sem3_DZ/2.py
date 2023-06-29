# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

text = "- Ах, не говорите мне про не Австрию! Я ничего не понимаю, может быть,\
но Австрия никогда не хотела и не хочет войны. Она предает нас. Россия одна\
должна быть спасительницей Европы. Наш благодетель знает свое высокое призвание\
и будет верен ему. Вот одно, во что я верю. Нашему доброму и чудному государю\
предстоит величайшая роль в мире, и он так добродетелен и хорош, что Бог\
не оставит его, и он исполнит свое призвание задавить гидру революции,\
которая теперь еще ужаснее в лице этого убийцы и злодея. Мы одни должны искупить\
кровь праведника. На кого нам надеяться, я вас спрашиваю?.. Англия с своим\
коммерческим духом не поймет и не может понять всю высоту души императора\
Александра. Она отказалась очистить Мальту. Она хочет видеть, ищет заднюю мысль\
наших действий. Что они сказали Новосильцеву? Ничего. Они не поняли, они не могли\
понять самоотвержения нашего императора, который ничего не хочет для себя и все\
хочет для блага мира. И что они обещали? Ничего. И что обещали, и того не будет!\
Пруссия уже объявила, что Бонапарте непобедим и что вся Европа ничего не может\
против него... И я не верю ни в одном слове ни Гарденбергу, ни Гаугвицу. Cette\
fameuse neutralité prussienne, ce n'est qu'un piège 9. Я верю в одного Бога и\
в высокую судьбу нашего милого императора. Он спасет Европу!.. — Она вдруг\
остановилась с улыбкой насмешки над своею горячностью."
# убираю мусор
format_text = text.replace(".", "")
format_text = format_text.replace("!", "")
format_text = format_text.replace(",", "")
format_text = format_text.replace("-", "")
format_text = format_text.replace("?", "")
format_text = format_text.lower()
# разбиваем по словам в Лист1
list1 = format_text.split()


# считаем вхождения слова результат в словарь res_dict - слово:кол-во
res_dict = {}
for i in list1:
    l = list1.count(i)
    res_dict[i] = l

# цикл для поиска 10 слов по кол-ву вхождений слов должнобыть обязательно более 10 и в список рес_лист
res_list = []
for _ in range(10):
    max_val = max(res_dict.values())
    # print(max_val)
    for key, val in res_dict.items():
        # print(";;;;")
        if val == max_val:
            res_list.append(key)
            # print(key)
            res_dict.pop(key)
            break
    # input()
print(res_list)
# # print(list1)