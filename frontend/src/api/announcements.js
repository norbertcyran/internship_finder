import api from './index';

export const getAnnouncements = () => {
    return api.get('/announcements/');
};

export const getAnnouncement = announcementId => {
    return api.get(`/announcements/${announcementId}/`);
};