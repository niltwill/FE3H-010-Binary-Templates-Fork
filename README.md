A fork of 010 binary templates (https://github.com/three-houses-research-team/010-binary-templates) from Three Houses Research Team

This fork is based on Triabolical's edits to the Three Houses Research Team's 010 binary template, which I cloned and made edits to for my personal use, so things such as the "Category: Reichard" was meant to organize the templates neatly in the templates selection list, not meant as taking ownership of the entire work.

This fork includes some updated information and files discovered by Triabolical ( https://github.com/triabolicals ) and myself, and I later plan to add just the new information/files (without the personal modifications) to the original repository.

In general it was refactored to improve file parsing speed, used clones of enums of different data sizes to be more accurate to the game code (which sometimes revealed some unknown functionality), attempting to clean up and be consistent, replacing char[numChars] with string, etc.

---

**niltwill:** I forked this to make it include everything from the original templates as well (so everything is in one place), to separate the scripts (.1sc format) from the rest, and to include some new ones. Feel free to reuse/include whatever you need. I didn't do a very thorough testing and experimentation - any updates & corrections are welcome.

Here is the list of the new/updated files:

* Enum/MonasteryNameID_enum.bt
* Map-Related/G1SharedStructures.bt
* Map-Related/OBJD.bt
* Model-Related/G2S.bt
* Scripts/SaveEntry_UpdateChecksum-RunTemplate.1sc
* Scripts/SaveSystem_UpdateChecksum-RunTemplate.1sc
* Scripts/save_updatechecksum.py
* 37.bt
* fixed_areadata.bt
* fixed_castle_regon_data.bt
* fixed_cut_in.bt
* fixed_gallery.bt
* fixed_onlinedata.bt
* fixed_scenario_abyss.bt
* fixed_stagedata.bt
* fixed_StageEnvInfo.bt
* fixed_tutorial.bt
* fixed_warpdata.bt
* MonasterySpawnData_bai.bt
* MonasteryTextData.bt
* person_monitor.bt
* saveSystem.bt

The most important addition (and what I was missing the most) would be the **MonasterySpawnData_bai.bt** - so now you can change the entities' (character) parameters during the monastery explorations. For example, to hide someone, set the "unavailable_flag" to 1. *Important:* you must re-enter the monastery exploration phase from the calendar (use an earlier save at the calendar), because using an existing save file during the exploration phase (of the chapter you're in) will not apply your changes (because it's already stored/cached in the save data - where exactly and how to nullify it is unknown for now).

**To be done:** update the event files on the basis of RE (or better yet, just use my GUI event editor). Eventually, do more RE and analysis of the model stuff too, besides G2S - that's quite hard though.
