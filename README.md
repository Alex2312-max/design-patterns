# design-patterns

### Laboratory Work 1

It was done in a form of a fantasy game and where the following design patterns were implemented:

- Factory method -> <font color='green'>tavern_factory.py</font>

- Abstarct factory method -> <font color='green'>sword_factory_method.py</font>

- Builder method -> <font color='green'>charcater_builder.py</font>


### Laboratory Work 2

For this laboratory work I decided to implement the following design patterns from the list provided:

- #### Adapter patter
  
  Adapter method was implemented inside a class, by manipulatinf 2 other classes that is basically an
  implementation of Factory design pattern. 
  
  ![image](https://user-images.githubusercontent.com/55151032/142229971-b585b8b9-7a46-46fb-8ebb-d6bca1897921.png)
  
  Here we have 2 different classes of monsters that both have a method of attack, but due to their different
  specialities, we can consider using different names for this methods, in such a way we use the Adapter method
  to get a more comfortable way of using this both classes simultaneously. The class 'MonsterSpawn' is called in
  the file 'abstract_factory.py' from the previous laboratory work
  
- #### Decorator pattern

  Decorator pattern was implemented superficially, but it shows the basic idea behind this type of 
  pattern.
  
  ![image](https://user-images.githubusercontent.com/55151032/142229498-43e68083-3c30-4527-892e-f9be13b78085.png)
  
  ![image](https://user-images.githubusercontent.com/55151032/142229553-8e30fcc9-09a2-4615-84d3-468d77fa1432.png)
  

- #### Proxy pattern - protection proxy;

  Proxy pattern was implemented independently from the general laboratory work, and represents
  a new feature in the improvised game a 'Bag' that holds different types of materials. The proxy 
  approach is observed and is represented by the fact that it is impossible to change the materials
  of the bag without the knowledge about the secret key.
  
  ![image](https://user-images.githubusercontent.com/55151032/142227946-294fb33a-4bec-48c1-b126-038e33838648.png)
  
  Even, if this code has a big security flaw, because of the password being stored in the source code and being
  stored as plain text this can serve as an example only.
  
  
