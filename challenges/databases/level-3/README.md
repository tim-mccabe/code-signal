# Overview of all Functions

## Suspects Investigation

A large amount of money was stolen today from the main city bank, and as the chief of police it's your duty to find the robber.

You store information about your suspects in the table **Suspect**, which has the structure:

* `id`: unique suspect id;
* `name`: suspect first name;
* `surname`: suspect surname;
* `height`: suspect height;
* `weight`: suspect weight.

You have already gathered some evidence and discovered the following clues:

* according to the camera records, the robber is not taller than `170cm`;
* the robber left their signature near the crime scene: `"B. Gre?n"`. `"B"` definitely stands for the first letter of robber's name, and `"Gre?n"` is their surname. The `4th` letter of the surname is smudged by ketchup and is unreadable.

To make the list of suspects smaller, you would like to filter out the suspects who can't possibly be guilty according to the information obtained from the clues. For each remaining suspect, you want to save his/her `id`, `name` and `surname`. Please note that the information obtained from the clue should be considered case-insensitive, so for example `"bill Green"`, and `"Bill green"`, and `"Bill Green"` should all be included in the new table.

Given the table **Suspect**, build the resulting table as follows: the table should have columns `id`, `name` and `surname` and its values should be ordered by the suspects' `ids` in ascending order.

#### Example

For the following table **Suspect**

| id | name     | surname | height | weight |
|----|----------|---------|--------|--------|
| 1  | John     | Doe     | 165    | 60     |
| 2  | Bill     | Green   | 170    | 67     |
| 3  | Baelfire | Grehn   | 172    | 70     |
| 4  | Bill     | Gretan  | 165    | 55     |
| 5  | Brendon  | Grewn   | 150    | 50     |
| 6  | bill     | Green   | 169    | 50     |

the output should be

| id | name    | surname |
|----|---------|---------|
| 2  | Bill    | Green   |
| 5  | Brendon | Grewn   |
| 6  | bill    | Green   |

The name of the `1st` suspect doesn't start with `"B"`, the `3rd` suspect is taller than `170cm`, and the surname of the `4th` suspect doesn't match the given pattern, meaning that these suspects are not included in the results.

## Suspects Investigation 2

A large amount of money was stolen today from the main city bank, and as the chief of police it's your duty to find the robber.

You store information about your suspects in the table **Suspect**, which has the structure:

* `id`: unique suspect id;
* `name`: suspect first name;
* `surname`: suspect surname;
* `height`: suspect height;
* `weight`: suspect weight.

You have already gathered some evidence and discovered the following clues:

* according to the camera records, the robber is taller than `170cm`;
* the robber left their signature near the crime scene: `"B. Gre?n"`. `"B"` definitely stands for the first letter of robber's name, and `"Gre?n"` is their surname. The `4th` letter of the surname is smudged by ketchup and is unreadable.

The clues you've obtained allow you to let some suspects go since they can't possibly be guilty, so now you need to build a list that contains the people who can be freed based on the gathered information. For each of these people, you need to know his/her `id`, `name` and `surname`. Please note that the information obtained from the clue should be considered case-insensitive, so for example `"bill Green"`, `"Bill GrEeN"`, and `"Bill Green"` should all be included in the new table.

Given the table **Suspect**, build the resulting table as follows: the table should have columns `id`, `name` and `surname` and its values should be ordered by the suspects' `ids` in ascending order.

#### Example

For the following table of **Suspect**

| id | name     | surname | height | weight |
|----|----------|---------|--------|--------|
| 1  | John     | Doe     | 165    | 60     |
| 2  | Bill     | Green   | 170    | 67     |
| 3  | Baelfire | Grehn   | 172    | 70     |
| 4  | Bill     | Gretan  | 185    | 55     |
| 5  | Brendon  | Grewn   | 180    | 50     |
| 6  | bill     | Green   | 172    | 50     |

the output should be

| id | name | surname |
|----|------|---------|
| 1  | John | Doe     |
| 2  | Bill | Green   |
| 4  | Bill | Gretan  |

The `1st` and the `2nd` suspects are not taller than `170cm`, and the `4th` suspect's surname doesn't match the `"Gre?n"` pattern, so these suspects can't be guilty.

## Security Breach

You are managing a large website that uses a special algorithm for user identification. In particular, it generates a unique attribute for each person based only on their first and last names and some additional metadata.

After analyzing the server logs today you found out that the website security has been breached and the data of some of your users might have been compromised.

The users' info is stored in the table **users** with the following structure:

* `first_name`: user's first name;
* `second_name`: user's last name;
* `attribute`: a unique attribute string of this user.

It seems that only the users those `attribute` was generated by the old version of your special algorithm were affected. Such attributes have the following format (accurate to *letter cases*): `<one or more arbitrary character>%<first name>_<second name>%<zero or more arbitrary characters>`. It's your duty now to warn the users that have these attributes about possible risks.

Given the **users** table, compose the resulting table consisting only of the rows that contain affected users' info. The result should be sorted by the `attributes` in *ascending* order.

#### Example

For the following table **users**

| first_name | second_name | attribute                                                           |
|------------|-------------|---------------------------------------------------------------------|
| Mikel      | Cover       | %Mikel_Cover%                                                       |
| Vicenta    | Kravitz     | 0%Vicenta_Kravitz%                                                  |
| Tosha      | Cover       | 02VO1aJ767GF7L186lpIfBR0fQ5406Q02YcpG42LDF4Bv26                     |
| Shayne     | Dahlquist   | 0R0V331K8Q7ypBi4Az3B6Nm0jCqUk%Shayne_Dahlquist%46E3O0u7t7           |
| Carrol     | Llanes      | 2mDIb1SdJne5wfH1Al32BE92r7j1d60PJ263b2vyPn3zxQ2P7sVOM26J11UT6W0Np   |
| Lizabeth   | Cover       | d1gM87S0NEHp386jXOk0aDc7w8bx4u8q7D82ff2Z4YT43iLyZ39xYbEDXMk         |
| Mack       | Chace       | fAnU49nMrmGu308627J7ne3qqqSPJDnq6dwW607lahNB5DinTR2Rkp549G7         |
| Vicenta    | Marchese    | kUJ3N67vLB07mQL9Ai7p18cXGzjdT32r8283ZQi                             |
| Mikel      | Kravitz     | PBX86iw1Ied87Z9OarE6sdSLdt%Mikel_Kravitz%W73XOY9YaOgi060r2x12D2EmD7 |
| Deirdre    | Chace       | PBX86iw1Ied87Z9OarE6sdSLdtDeirdrelChaceW73XOY9YaOgi060r2x12D2EmD7   |
| Josphine   | Arzate      | PwWD95BCKVYn5YD7iHLMa3HjP9tH%josphine_arzate%d2hNHNd3RpqfUREN47     |
| Deirdre    | Chace       | ryCE5FIyS8q54A5036luzVS91j6C7P76E9X0O58htzgthuX24LG%DEirdre_Chace%  |
| Julietta   | Beer        | Tn35g5h51u7ltW946J                                                  |

the output should be

| first_name | second_name | attribute                                                           |
|------------|-------------|---------------------------------------------------------------------|
| Vicenta    | Kravitz     | 0%Vicenta_Kravitz%                                                  |
| Shayne     | Dahlquist   | 0R0V331K8Q7ypBi4Az3B6Nm0jCqUk%Shayne_Dahlquist%46E3O0u7t7           |
| Mikel      | Kravitz     | PBX86iw1Ied87Z9OarE6sdSLdt%Mikel_Kravitz%W73XOY9YaOgi060r2x12D2EmD7 |