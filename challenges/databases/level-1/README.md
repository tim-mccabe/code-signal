# Overview of all Functions

## Project List

Your boss wants to identify the successful projects running in your company, so he asked you to prepare a list of all the currently active projects and their average monthly income.

You have stored the information about these projects in a simple database with a single **Projects** table that has five columns:

* **internal_id**: the company's internal identifier for the project;
* **project_name**: the official name of the project;
* **team_size**: the number of employees working on the project;
* **team_lead**: the name of the project manager;
* **income**: the average monthly income of the project.
Your boss says that internal project ids are irrelevant to him and that he isn't interested in how big the teams are. Since that's the case, he wants you to create another table by removing the **internal_id** and **team_size** columns from the existing **Projects** table. Return it sorted by `internal_id` in ascending order.

#### Example

For the following table **Projects**

| internal_id | project_name | team_size |   team_lead  | income |
|:-----------:|:------------:|:---------:|:------------:|:------:|
| 1384        | MapReduce    | 100       | Jeffrey Dean | 0      |
| 2855        | Windows      | 1000      | Bill Gates   | 100500 |
| 5961        | Snapchat     | 3         | Evan Spiegel | 2000   |

the resulting table should be

| project_name |   team_lead  | income |
|:------------:|:------------:|:------:|
| MapReduce    | Jeffrey Dean | 0      |
| Windows      | Bill Gates   | 100500 |
| Snapchat     | Evan Spiegel | 2000   |

## Countries Selection

Your friend wants to become a professional tour guide and travel all around the world. In pursuit of this dream, she enrolled in tour guide school. The professors in this school turned out to be very demanding, and one of them gave your friend a difficult assignment that she has to finish over the weekend.

Here's the assignment: Given a list of countries, your friend should identify all the countries that are in Africa. To help her, you have decided to write a function that will find all such countries from any set of countries. The **countries** table in which the countries are stored has the following structure:

* `name`: the name of the country;
* `continent`: the continent on which the country is situated;
* `population`: the country's population.

Your task is to return a new table that has the same columns, but that only contains the countries from Africa. The countries should be sorted alphabetically by their names.

#### Example

For the following table **countries**

| name     | continent     | population |
|----------|---------------|------------|
| Austria  | Europe        | 8767919    |
| Belize   | North America | 375909     |
| Botswana | Africa        | 2230905    |
| Cambodia | Asia          | 15626444   |
| Cameroon | Africa        | 22709892   |

the output should be

| name     | continent | population |
|----------|-----------|------------|
| Botswana | Africa    | 2230905    |
| Cameroon | Africa    | 22709892   |

## Monthly Scholarships

Students at your university get scholarships that are paid out throughout the year.

Information about the scholarships is stored in the table **scholarships**, which has the structure:

* `id`: the unique student id;
* `scholarship`: the amount of the annual scholarship the student has been awarded.

Now you need to calculate the amount of money each student should get per month. Given the table **scholarships**, build the resulting table as follows: The table should have the same columns as the initial table, but the `scholarship` column should contain the amount of the student's monthly scholarship payout. The rows should be ordered by the students' `id`s.

#### Example

For the following table **scholarships**

| id | scholarship |
|----|-------------|
| 1  | 12000       |
| 2  | 18000       |
| 3  | 24000       |
| 4  | 15000       |
| 5  | 21000       |
| 6  | 13000       |

the output should be

| id | scholarship        |
|----|--------------------|
| 1  | 1000               |
| 2  | 1500               |
| 3  | 2000               |
| 4  | 1250               |
| 5  | 1750               |
| 6  | 1083.3333333333333 |

## Projects Team

You've been promoted and assigned to a new project. The problem is, you don't know who you are working with and your predecessor has vanished without a trace! Luckily, each project in your company keeps its own activity database, which you are going to use to find out the names of your new colleagues.

Information about the project's activity is stored in table **projectLog**, which has the following structure:

* `id`: unique action id;
* `name`: the name of the person who performed the action;
* `description`: the description of the action;
* `timestamp`: the timestamp of the action.

You only have access to the project's most recent history, but this should be enough for you. You've decided that finding everyone who interacted with the project in this period is the best way to start.

Given the table **projectLog**, build a new results table with a single `name` column that contains the names of the project's contributors sorted in ascending order.

#### Example

For the following table **projectLog**

| id | name             | description           | timestamp           |
|----|------------------|-----------------------|---------------------|
| 1  | James Smith      | add new logo          | 2015-11-10 15:24:32 |
| 2  | John Johnson     | update license        | 2015-11-10 15:50:01 |
| 3  | John Johnson     | fix typos             | 2015-11-10 15:55:01 |
| 4  | James Smith      | update logo           | 2015-11-10 17:53:04 |
| 5  | James Smith      | delete old logo       | 2015-11-10 17:54:04 |
| 6  | Michael Williams | fix the build         | 2015-11-12 13:37:00 |
| 7  | Mary Troppins    | add new feature       | 2015-11-08 17:54:04 |
| 8  | James Smith      | fix fonts             | 2015-11-14 13:54:04 |
| 9  | Richard Young    | remove unneeded files | 2015-11-14 00:00:00 |
| 10 | Michael Williams | add tests             | 2015-11-09 11:53:00 |

the output should be

| name             |
|------------------|
| James Smith      |
| John Johnson     |
| Mary Troppins    |
| Michael Williams |
| Richard Young    |

## Automatic Notifications

The application you've been working on for the past year is a huge success! It already has a large and active user community. You know the ID number, username, and email of each user. Each user also has a specific role that shows their position in the community. Information about the users is stored in the database as a table **users**, which has the following structure:

* `id`: the unique user ID;
* `username`: the username of the user;
* `role` the user's role;
* `email`: the user's email.

You want to send users automatic notifications to let them know about the most recent updates. However, not all users should get these notifications: Administrators don't need notifications since they know about the updates already, and premium users don't need them since they get personalized weekly updates.

Given the **users** table, your task is to return the emails of all the users who should get notifications, i.e. those whose `role` is not equal to `"admin"` or `"premium"`. Note that roles are case insensitive, so users with `role`s of `"Admin"`, `"pReMiUm"`, etc. should also be excluded.

The resulting table should contain a single `email` column and be sorted by `email`s in ascending order.

#### Example

For the following table **users**

| id | username     | role    | email                   |
|----|--------------|---------|-------------------------|
| 6  | fasalytch    | premium | much.premium@role.com   |
| 13 | luckygirl    | regular | fun@meh.com             |
| 16 | todayhumor   | guru    | today@humor.com         |
| 23 | Felix        | admin   | felix@codesignal.com    |
| 52 | admin666     | AdmiN   | iamtheadmin@admin.admin |
| 87 | solver100500 | regular | email@notbot.com        |

the resulting table should be

| email            |
|------------------|
| email@notbot.com |
| fun@meh.com      |
| today@humor.com  |