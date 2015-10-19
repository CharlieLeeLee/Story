###CSC 210
#Project Milestone 1: Project Proposal
###Group Members: [Charlie Norvell] (mailto:anorvell@u.rochester.edu) [Lucinda Liu] (mailto:yliu114@u.rochester.edu)

##Story
Our Web Application’s name is Story. This name is based on what our main usage of this web will be: the collaborative creation of stories.

##Target Audience
The target audience for this web is people who want to show their talent in writing stories, who want to construct a story with other writers, who want to share 
story ideas to see them unfold into a full novel or screenplay, and who just have interest in writing. 

##The Problem
So, what will Story do for this audience? Our web appwill have two main parts. First, each user can create an account and, using that account, 
they can write and their short story, novel, poem, or script. The main purpose the app is creative writing, so it’s not like a blog for sharing your life story. 
Of course, if you want to write your own life story as a memoir or something, it’s totally fine. 
When posting their writing, the user can choose to make it public or private. Other users will be able view the story can comment on it. What’s more, 
if anyone wants to make a film or otherwise use someone's story outside of the app, they can easily contact the owner through our app.
 	
For the second part, which is what makes our app unique, writing that is posted publicly will be open to collaboration. Like a Google Doc, 
users that have access to a posted piece of writing will be able to edit it. 
The heart of our app is that every account member can choose to write a story idea or a beginning of a story on this platform, and others can take that idea or
snippet and expand on it. Each story will be a product of the community much like open source software.
Users can also have discussions in the comments, making this a great community for people that share an interest and talent for writing.

##Project Requirements
This will definitely meet the minimum requirements for the project. First, to use the app, users must create an account In this account, they will have a profile, 
which can include a short bio and their writing experience. Second, we will store the story and the account information on the server, so we need to read the data from 
the server to show other users. For each story, owners can always edit it, update it, or delete it. And lastly, we will do all the things above in Ajax, 
since we would like to allow multiple users to edit the files at the same time, and reloading the page for each update would be too much work.
As the latter feature will probably be fairly complicated, we will also be using Ajax for our comment/messaging system.

##Stretch Goals
If we are able to accomplish the above and have extra time, we would like to also implement:
* More extensive profile pages
* Private messaging system