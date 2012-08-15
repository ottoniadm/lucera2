# Made by Mr. - Version 0.3 by DrLecter
import sys
from ru.catssoftware.gameserver.model.quest import State
from ru.catssoftware.gameserver.model.quest import QuestState
from ru.catssoftware.gameserver.network.serverpackets import SocialAction
from ru.catssoftware.gameserver.model.quest.jython import QuestJython as JQuest

qn = "261_DreamOfMoneylender1"

GIANT_SPIDER_LEG = 1087
ADENA = 57

class Quest (JQuest) :

 def __init__(self,id,name,descr): 
     JQuest.__init__(self,id,name,descr)
     self.questItemIds = [GIANT_SPIDER_LEG]

 def onEvent (self,event,st) :
    htmltext = event
    if event == "30222-03.htm" :
      st.set("cond","1")
      st.setState(State.STARTED)
      st.playSound("ItemSound.quest_accept")
    return htmltext

 def onTalk (self,npc,player):
   htmltext = "<html><body>You are either not on a quest that involves this NPC, or you don't meet this NPC's minimum quest requirements.</body></html>"
   st = player.getQuestState(qn)
   if not st : return htmltext

   npcId = npc.getNpcId()
   id = st.getState()

     st.set("cond","0")
   if st.getInt("cond")==0 :
     if player.getLevel() >= 15 :
       htmltext = "30222-02.htm"
     else:
       htmltext = "30222-01.htm"
       st.exitQuest(1)
   else :
     if st.getQuestItemsCount(GIANT_SPIDER_LEG) >= 8 :
       st.rewardItems(ADENA,1000)
       st.takeItems(GIANT_SPIDER_LEG,-1)
       st.addExpAndSp(2000,0)
       ObjectId=player.getObjectId()
       player.broadcastPacket(SocialAction(ObjectId,3))
       htmltext = "30222-05.htm"
       st.checkNewbieQuests()
       st.exitQuest(1)
       st.playSound("ItemSound.quest_finish")
     else:
       htmltext = "30222-04.htm"
   return htmltext

 def onKill(self,npc,player,isPet):
   st = player.getQuestState(qn)
   if not st : return
   if st.getState() != State.STARTED : return
   
   count = st.getQuestItemsCount(GIANT_SPIDER_LEG)
   if count < 8 :
     st.giveItems(GIANT_SPIDER_LEG,1)
     if count == 7 :
       st.playSound("ItemSound.quest_middle")
       st.set("cond","2")
     else:
       st.playSound("ItemSound.quest_itemget")
   return

QUEST       = Quest(261,qn,"Collector's Dream")

QUEST.addStartNpc(30222)

QUEST.addTalkId(30222)

QUEST.addKillId(20308)
QUEST.addKillId(20460)
QUEST.addKillId(20466)