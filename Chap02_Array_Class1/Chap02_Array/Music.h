#pragma once        // 중복안되게 붙여줌
#include <iostream> 
#include <string>
#include <vector>

using namespace std;

// Music class
class Music {
private:
    string title;
    string artist;
    string album;
    int year;
public:
    //생성자(Constructor)
    Music(string title, string artist, string album, int year) {
        this->title = title;
        this->artist = artist;
        this->album = album;
        this->year = year;
    }
    //소멸자(Destructor)
    ~Music() {}

    // Getters
    string getTitle() { 
        return title; 
    }
    string getArtist() { 
        return artist; 
    }
    string getAlbum() { 
        return album; 
    }
    int getYear() { 
        return year; 
    }
};

// MusicStreamingService class
class MusicStreamingService {
private:
    string serviceName;
    vector<Music> musicList;

public:
    // 생성자
    MusicStreamingService(string serviceName) {
        this->serviceName = serviceName;
    }

    // Adds a music to the service
    void addMusic(string title, string artist, string album, int year) {
        Music newMusic(title, artist, album, year);
        musicList.push_back(newMusic); //neWMusic을추가해주는 함수 push_back
        cout << title << " by " << artist << " added to " << serviceName << endl;
    }

    // Searches for music by title
    Music* searchByTitle(string title)  {
        for (int i = 0; i < musicList.size(); i++) //0번째 함수
        {
            if (musicList[i].getTitle() == title) {
                return &musicList[i];
            }
        }
        return NULL;
    }

    // Searches for music by artist
    vector<Music*> searchByArtist(string artist) {
        vector<Music*> result;
        for (int i = 0; i < musicList.size(); i++) {
            if (musicList[i].getArtist() == artist) {
                result.push_back(&musicList[i]);
            }
        }
        return result;
    }

};

