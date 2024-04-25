import AvatarGroup from '@mui/joy/AvatarGroup';
import Avatar from '@mui/joy/Avatar';
import Box from '@mui/joy/Box';
import Button from '@mui/joy/Button';
import Typography from '@mui/joy/Typography';
import ArrowForward from '@mui/icons-material/ArrowForward';
import TwoSidedLayout from '../mainComponents/TwoSidedLayout';
import { Link } from 'react-router-dom';

export default function HeroLeft03() {
  return (
    <TwoSidedLayout>
      <Typography color="primary" fontSize="lg" fontWeight="lg">
        The power to do more
      </Typography>
      <Typography
        level="h1"
        fontWeight="xl"
        fontSize="clamp(1.875rem, 1.3636rem + 2.1818vw, 3rem)"
      >
        A large headlinerer about our product features & services
      </Typography>
      <Typography fontSize="lg" textColor="text.secondary" lineHeight="lg">
        A descriptive secondary text placeholder. Use it to explain your business
        offer better.
      </Typography>
      <Box
        sx={{
          display: 'flex',
          flexWrap: 'wrap',
          gap: 2,
          my: 2,
          '& > *': { flex: 'auto' },
        }}
      >
        <Link to="/signup" style={{ textDecoration: 'none' }}>
          <Button size="lg" variant="outlined" color="neutral">
            Sign up
          </Button>
          </Link>
        <Link to="/login" style={{ textDecoration: 'none' }}>
          <Button size="lg" endDecorator={<ArrowForward />}>
            Log in
          </Button>
        </Link>
      </Box>
      <Box
        sx={{
          display: 'flex',
          flexWrap: 'wrap',
          justifyContent: 'center',
          gap: 2,
          textAlign: 'left',
          '& > *': {
            flexShrink: 0,
          },
        }}
      >
        <AvatarGroup size="lg">
          <Avatar />
          <Avatar />
          <Avatar />
        </AvatarGroup>
        <Typography textColor="text.secondary">
          Join a community of over <b>10K</b> <br />
          designers and developers.
        </Typography>
      </Box>

    </TwoSidedLayout>
  );
}
