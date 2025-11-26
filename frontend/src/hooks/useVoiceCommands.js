import { useNavigate } from 'react-router-dom';

// This hook returns the command configuration for react-speech-recognition
export const useVoiceCommands = () => {
  const navigate = useNavigate();

  const commands = [
    {
      // Matches commands in English or Hindi for internships page
      command: ['Go to internships', 'इंटर्नशिप दिखाओ', 'इंटर्नशिप पर जाएं'],
      callback: (...args) => {
        console.log("Voice command recognized: INTERNSHIPS", args);
        navigate('/internships');
      },
      matchInterim: true, // For faster response
    },
    {
      // Matches "Go home" or Hindi equivalents for the home page
      command: ['Go home', 'वापस जाओ', 'होम पर जाएं'],
      callback: (...args) => {
        console.log("Voice command recognized: HOME", args);
        navigate('/');
      },
      matchInterim: true,
    },
    // You can add more navigation commands here
  ];

  return { commands };
};
