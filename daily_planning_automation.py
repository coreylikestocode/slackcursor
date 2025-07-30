#!/usr/bin/env python3
"""
Daily Planning Automation Script
Helps create and maintain daily planning habits with reminders and quick templates.
"""

import datetime
import os
import subprocess
import sys
from pathlib import Path

def get_tomorrow_date():
    """Get tomorrow's date in a readable format."""
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    return tomorrow.strftime("%A, %B %d, %Y")

def create_daily_plan_file():
    """Create a new daily plan file for tomorrow."""
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    filename = f"daily_plan_{tomorrow.strftime('%Y%m%d')}.md"
    
    template_content = f"""# Daily Plan - {get_tomorrow_date()}

## 🎯 Today's Highlight (Most Important Task)
*What ONE thing would make today feel successful?*

**MY DAILY HIGHLIGHT:**


## ⏰ Time Blocks

| Time | Activity | Type | Energy Level |
|------|----------|------|--------------|
| 6:00 AM | Morning routine | Personal | Low |
| 7:00 AM |  |  |  |
| 8:00 AM |  |  |  |
| 9:00 AM |  |  |  |
| 10:00 AM |  |  |  |
| 11:00 AM |  |  |  |
| 12:00 PM | Lunch | Personal | Low |
| 1:00 PM |  |  |  |
| 2:00 PM |  |  |  |
| 3:00 PM |  |  |  |
| 4:00 PM |  |  |  |
| 5:00 PM |  |  |  |
| 6:00 PM | Evening routine | Personal | Low |

## 📅 Scheduled Meetings & Events
- [ ] **Meeting 1:** _____________ (Time: ___, Prep needed: ___)
- [ ] **Meeting 2:** _____________ (Time: ___, Prep needed: ___)
- [ ] **Event/Appointment:** _____________ (Time: ___)

## ✅ Priority Tasks (Top 3)
1. **[HIGH]** 
2. **[MEDIUM]** 
3. **[LOW]** 

## 📧 Email & Communication Action Items
- [ ] 
- [ ] 
- [ ] 

## 🚧 Potential Obstacles & Backup Plans
**Likely interruptions:**
**If running behind, I will:**
**Emergency delegate list:**

## 🎉 End of Day - Success Metrics
*I'll consider today successful if I complete:*
- [ ] My daily highlight
- [ ] At least 2 priority tasks
- [ ] All scheduled meetings prepared and attended

---
*Created: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""

    with open(filename, 'w') as f:
        f.write(template_content)
    
    print(f"✅ Created daily plan: {filename}")
    return filename

def create_weekly_planning_template():
    """Create a weekly planning template."""
    today = datetime.date.today()
    # Get Monday of this week
    monday = today - datetime.timedelta(days=today.weekday())
    week_start = monday.strftime("%B %d")
    week_end = (monday + datetime.timedelta(days=6)).strftime("%B %d, %Y")
    
    filename = f"weekly_plan_{monday.strftime('%Y%m%d')}.md"
    
    template_content = f"""# Weekly Plan - {week_start} to {week_end}

## 🎯 This Week's Main Goals
1. 
2. 
3. 

## 📅 Weekly Schedule Overview

### Monday
- **Highlight:** 
- **Key meetings:** 
- **Focus area:** 

### Tuesday
- **Highlight:** 
- **Key meetings:** 
- **Focus area:** 

### Wednesday
- **Highlight:** 
- **Key meetings:** 
- **Focus area:** 

### Thursday
- **Highlight:** 
- **Key meetings:** 
- **Focus area:** 

### Friday
- **Highlight:** 
- **Key meetings:** 
- **Focus area:** 

## 🔄 Recurring Weekly Tasks
- [ ] Team check-ins
- [ ] Weekly review
- [ ] Planning for next week
- [ ] 

## 📈 Weekly Review Questions
*Complete at end of week:*

**What went well this week?**


**What could be improved?**


**What are the priorities for next week?**


---
*Created: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""

    with open(filename, 'w') as f:
        f.write(template_content)
    
    print(f"✅ Created weekly plan: {filename}")
    return filename

def quick_planning_session():
    """Run a quick interactive planning session."""
    print("\n🎯 Quick Daily Planning Session")
    print("=" * 40)
    
    # Get tomorrow's highlight
    highlight = input("\n1. What's your ONE most important task for tomorrow?\n   > ")
    
    # Get top 3 priorities
    print("\n2. What are your top 3 priorities? (Press Enter after each)")
    priority1 = input("   Priority 1: ")
    priority2 = input("   Priority 2: ")
    priority3 = input("   Priority 3: ")
    
    # Get meeting count
    meetings = input("\n3. How many meetings/appointments do you have tomorrow? ")
    
    # Get energy planning
    print("\n4. When is your highest energy time? (e.g., 9-11 AM)")
    energy_time = input("   > ")
    
    # Create quick summary
    tomorrow_date = get_tomorrow_date()
    
    summary = f"""
📋 TOMORROW'S PLAN SUMMARY - {tomorrow_date}
{'=' * 50}

🎯 DAILY HIGHLIGHT: {highlight}

✅ TOP PRIORITIES:
   1. {priority1}
   2. {priority2}  
   3. {priority3}

📅 MEETINGS: {meetings} scheduled

⚡ HIGH ENERGY TIME: {energy_time}
   → Schedule your highlight during this time!

💡 REMINDER: Plan tonight, win tomorrow!
"""
    
    print(summary)
    
    # Save to file
    save = input("\nSave this plan to a file? (y/n): ").lower().strip()
    if save == 'y':
        filename = create_daily_plan_file()
        with open(filename, 'a') as f:
            f.write(f"\n\n<!-- Quick Planning Session Results -->\n{summary}")
        print(f"✅ Plan saved and appended to {filename}")

def show_planning_tips():
    """Display helpful planning tips."""
    tips = """
🏆 DAILY PLANNING SUCCESS TIPS
================================

⏰ TIMING:
   • Plan tomorrow tonight (5 minutes before bed)
   • Review and adjust in the morning (2 minutes)

🎯 PRIORITIZATION:
   • Choose ONE daily highlight (most important task)
   • Use the "Eat the Frog" method (hardest task first)
   • Apply 80/20 rule (focus on high-impact activities)

📅 TIME MANAGEMENT:
   • Time-block your calendar
   • Add 25% buffer time to estimates  
   • Batch similar tasks together
   • Protect your peak energy hours

🚧 CONTINGENCY PLANNING:
   • Identify potential interruptions
   • Have a "Plan B" for each important task
   • Know what you can delegate or postpone

🔄 CONTINUOUS IMPROVEMENT:
   • Do a 5-minute end-of-day review
   • Track what works and what doesn't
   • Adjust your system weekly

📱 TOOLS INTEGRATION:
   • Sync with your existing calendar app
   • Use phone reminders for planning sessions
   • Keep templates accessible
"""
    print(tips)

def main():
    """Main menu for the daily planning automation."""
    print("🗓️  DAILY PLANNING AUTOMATION")
    print("=" * 35)
    print("1. Create tomorrow's daily plan")
    print("2. Create weekly planning template")
    print("3. Quick planning session (interactive)")
    print("4. Show planning tips")
    print("5. Exit")
    
    while True:
        try:
            choice = input("\nChoose an option (1-5): ").strip()
            
            if choice == '1':
                create_daily_plan_file()
            elif choice == '2':
                create_weekly_planning_template()
            elif choice == '3':
                quick_planning_session()
            elif choice == '4':
                show_planning_tips()
            elif choice == '5':
                print("📅 Happy planning! Remember: 5 minutes of planning saves 25 minutes of execution.")
                break
            else:
                print("❌ Please choose a number between 1-5")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Keep planning for success!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()