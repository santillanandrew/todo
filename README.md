# todo
A Terminal-based command set for those who prefer a clutter-free list of TODOs. 

## Modifications
The path names in `todo.py` and `custom_commands.sh` are relevant to my computer. You'll need to update these path names to reflect the correct locations of `todo.py` and `todo.txt` on your computer. 

Terminal doesn't recognize the shell function in `custom_commands.sh` on its own. You've gotta create a zshrc file and source `custom_commands.sh`. The path name for `custom_commands.sh` in `.zshrc` is also specific to my computer, so don't forget to update that. 

## Usage

You can add an event to the TODO list in chronological order with `todo newev "{Event}" on "{Month} {DD}, {YYYY}"`

You can add an item to the TODO list with `todo newit "{Item}"`

You can delete an event from the TODO list with `todo delev "{Event}"`

You can clear the TODO list with `todo clear`

You can display the TODO list with `todo show`
