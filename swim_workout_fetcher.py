"""
Swim Dojo Workout Fetcher
Fetches random swim workouts from swimdojo.com
Based on: https://www.reddit.com/r/Swimming/comments/1dtzus8/i_made_a_script_that_opens_a_random_swim_workout/
"""

import webbrowser
import random
import requests
from bs4 import BeautifulSoup


def get_workout_tags():
    """Fetch available workout tags from swimdojo.com"""
    try:
        url = "https://www.swimdojo.com/workouts"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all tag links (adjust selector based on actual site structure)
        tags = []
        tag_elements = soup.find_all('a', href=lambda x: x and '/workouts/tag/' in x)
        
        for element in tag_elements:
            tag = element.get('href').split('/workouts/tag/')[-1]
            if tag and tag not in tags:
                tags.append(tag)
        
        return tags if tags else ['sprint', 'endurance', 'technique', 'im', 'distance']
    except Exception as e:
        print(f"Error fetching tags: {e}")
        # Return default tags if fetching fails
        return ['sprint', 'endurance', 'technique', 'im', 'distance']


def get_workouts_by_tag(tag):
    """Fetch workout URLs for a specific tag"""
    try:
        url = f"https://www.swimdojo.com/workouts/tag/{tag}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all workout links
        workouts = []
        workout_links = soup.find_all('a', href=lambda x: x and '/workouts/' in x and '/tag/' not in x)
        
        for link in workout_links:
            href = link.get('href')
            if href.startswith('/'):
                href = 'https://www.swimdojo.com' + href
            elif not href.startswith('http'):
                href = 'https://www.swimdojo.com/workouts/' + href
            
            if href not in workouts and href != 'https://www.swimdojo.com/workouts':
                workouts.append(href)
        
        return workouts
    except Exception as e:
        print(f"Error fetching workouts for tag '{tag}': {e}")
        return []


def open_random_workout(tag=None):
    """
    Open a random workout from swimdojo.com in the default browser
    
    Args:
        tag (str, optional): Specific workout tag to filter by. If None, uses random tag.
    
    Returns:
        str: The URL that was opened, or None if failed
    """
    try:
        if tag is None:
            tags = get_workout_tags()
            if not tags:
                print("No tags available")
                return None
            tag = random.choice(tags)
            print(f"Selected random tag: {tag}")
        
        workouts = get_workouts_by_tag(tag)
        
        if not workouts:
            print(f"No workouts found for tag: {tag}")
            return None
        
        workout_url = random.choice(workouts)
        print(f"Opening workout: {workout_url}")
        webbrowser.open(workout_url)
        
        return workout_url
    except Exception as e:
        print(f"Error opening random workout: {e}")
        return None


if __name__ == "__main__":
    print("Swim Dojo Workout Generator")
    print("=" * 40)
    
    # Try to get a random workout
    result = open_random_workout()
    
    if result:
        print(f"\nSuccessfully opened: {result}")
    else:
        print("\nFailed to open workout. Please check your internet connection.")
