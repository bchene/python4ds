# Python Oriented Object Programming

### SUBJECT
Create an abstract class "character" which can take a first_name as first parameter,
is_alive as second non mandatory parameter set to True by default and can change the
health state of the character with a method that passes is_alive from True to False.
And a "stark" class which inherits from Character

### SUJET
Cree une classe abstraite "character"
qui peut prendre un prenom comme premier parametre,
is_alive comme second parametre non obligatoire set a True par defaut
et peut changer l'etat de la santé du personnage avec une methode
qui passe is_alive de True a False.
Et une classe "stark" qui herite de Character

### ABC : Abstract Base Class
abstractmethod : Methode abstraite  
ABCMeta : Meta classe pour les classes abstraites  
abstractproperty : Propriete abstraite  
abstractclassmethod : Methode de classe abstraite  
abstractmethod : Methode abstraite  

### @classmethod :
Une METHODE de CLASSE qui est partagee par toutes les instances de la classe.  
Elle est definie dans la classe et non dans les instances.  
Elle est utilisee pour creer de nouvelles instances de la classe.  
Elle est definie avec le decorateur @classmethod.  
Elle est utilisee avec le nom de la classe et non avec le nom de l'instance.  
Elle est utilisee avec le parametre cls pour faire reference a la classe.  
Elle est utilisee avec le parametre *args pour faire reference aux arguments.  
Elle est utilisee avec le parametre **kwargs pour faire reference aux arguments.  

### @staticmethod :
Une METHODE STATIQUE qui est partagee par toutes les instances de la classe.  
Elle est definie dans la classe et non dans les instances.  
Elle est utilisee pour creer de nouvelles instances de la classe.  
Elle est definie avec le decorateur @staticmethod.  
Elle est utilisee avec le nom de la classe et non avec le nom de l'instance.  
Elle est utilisee avec le parametre cls pour faire reference a la classe.  
Elle est utilisee avec le parametre *args pour faire reference aux arguments.  
Elle est utilisee avec le parametre **kwargs pour faire reference aux arguments.  

### @abstractmethod :
Un METHODE ABSTRAITE est une methode qui doit etre implementee dans les classes filles  
et qui ne peut pas etre implementee dans la classe.  
Elle est definie avec le decorateur @abstractmethod.  
Elle est utilisee avec la methode abstractmethod.  
Il est utilise pour modifier le comportement d'une fonction sans la modifier.  
Il est defini avec le decorateur @abstractmethod.  
Il est utilise avec la methode abstractmethod.  
