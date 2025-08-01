# System Improvement Suggestions — Pango Pay & Go

This document outlines proposed enhancements to improve the usability, stability, and user experience of the **Pango Pay & Go Parking Lot Manager**.

---

## 1. Time Zone Handling  
**Issue**: Parking session timestamps are not aligned with local time (Israel Standard Time).  
**Suggestion**: Use time zone-aware datetime formatting via backend and frontend to ensure consistency.

---

## 2. Contextual Alerts  
**Issue**: Alerts (error/success) appear globally on the dashboard, even if the action was triggered in a different page.  
**Suggestion**: Render alerts within the relevant page where the action occurred for clarity.

---

## 3. User Management System  
**Issue**:  
- The "Delete User" button is clickable even when the user has parking sessions.  
- No permissions system exists to control who can manage users.

**Suggestion**:  
- Disable the delete button for users with sessions.  
- Implement a **role-based access control system**, where only users with `admin` roles can add/edit/delete other users.  
- Include UI indicators to clearly show which users are system administrators.  

---

## 4. Mobile Responsiveness  
**Issue**: The system UI is not optimized for small screens or tablets.  
**Suggestion**: Apply responsive design 

---

## 5. Visual Improvements & UX Enhancements  
**Issue**: Current UI layout is minimal and lacks visual polish.  
**Suggestion**:
- Improve button and alerts styling and spacing for better accessibility.
- Use modals or confirmation dialogs for sensitive actions.
- Improve history table: clearer headers, readable date format, alternating row colors and etc
- Enhance end-parking flow: more prominent button, confirmation dialog before ending, and summary of the session.

---

## 6. History Filtering & Search  
**Issue**: The History table lacks filtering or search functionality.  
**Suggestion**:  
- Add filters by plate number, user, or date.  
- Implement a search bar for real-time results.  
- Support sorting columns




