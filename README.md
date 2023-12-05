for use with [windtracker](https://github.com/vncz14/windtracker-vue). forked from [Toufool/AutoSplit](https://github.com/Toufool/AutoSplit)

# how 2 use
- set split image folder to `img/splits`

- settings > hotkey settings
  - set your livesplit hotkeys
  - make sure global hotkeys is on in livesplit

- settings > capture settings
  - max fps 60
  - capture method to bitblt
    - for now thats the only one i bothered to support

- settings > image settings
  - comparison method histograms
  - similarity threshold 1
  - pause threshold as high as it can go while still working, i didnt bother to find out the exact number of seconds

- settings > windtracker settings
  - windtracker mode on
  - mph on if you're on ntsc
  - set speed image folder to `img/speeds`, direction image folder to `img/directions`
    - we need more accurate images send a pr pls
  - open resort a
    - in the main menu line up the region as well inside the wind circle as possible like this
      ![001_SplitImage](https://github.com/vncz14/AutoSplit-windtracker/assets/57498723/20361999-1dd9-4ace-a351-8d03e0118ecd)
    - set the x, y, width and height inside region 1
  - same with resort b and region 2
 
- actually using it
  - open [windtracker](https://github.com/vncz14/windtracker-vue)
  - click on text mode
  - press your livesplit start hotkey
      
